-------------------------
- SOLVING A TEST TASKS: -
-------------------------

1) Please write iptables rules that will block all incoming traffic and allow outgoing (browsing from local machine should work, but all incoming connections should be dropped).

how to do:
    1)	Setting up policies for dropping all incoming and forwarding packets:
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP

    2)	Setting up rules for accepting outgoing packets:
sudo iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT

# iptables -L
Chain INPUT (policy DROP)
target     prot opt source               destination
ACCEPT     all  --  anywhere             anywhere             state RELATED,ESTABLISHED

Chain FORWARD (policy DROP)
target     prot opt source               destination
ACCEPT     all  --  anywhere             anywhere             state RELATED,ESTABLISHED

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination

*****************************************************************************************************************************

2) There is a directory with 2 files that are shown as '???' and '???'. They have different names, but in console are shown as 3 question marks. How to remove them?

Perhaps it happened because something wrong to the encoding. The best way to remove that files is to use their inodes. For example:
# ls -il
# 17486817 -rw-r--r--. 1 root root 0 Mar 19 12:32 ???
# 17486837 -rw-r--r--. 1 root root 0 Mar 19 12:32 ???
# for inod in 17486817 17486837; do find . -inum $inod -delete; done


*******************************************************************************************************************************

3) If you want to upload some file once per hour to 1 server from 1000 servers, how it can be done? What special cases should be taken into account?


For upload each hour to 1 of 1000s servers we can use ansible.

We might run related playbook from script, which
    -	counts steps from zero up to max_servers and from zero again (it changes index each time/hour);
    -	finds to the current server’s number according to index;
    -	constructs new inventory file according to the address of the desired host;
    -	runs ansible playbook;
    -	writes result to file Hosts_DONE.txt;
    -	changes index to next (or to zero if index reached server’s maximum).
We need to configure the crontab according to these settings (for run it automatically hour by hour):

    0 */1 * * * cd <SCRIPT_DIR>/ && ./run_copy.py

If something happened to the fingerprint on the target host, we can see these requests:

The authenticity of host ***** can't be established.
RSA key fingerprint is *****.
Are you sure you want to continue connecting (yes/no)?

Or 

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that the RSA host key has just been changed.
The fingerprint for the RSA key ......

To avoid this, we need to use the keys:

host_key_checking = False in ./ansible.cfg

we also need to pay attention to the users, passwords, and access rights on the target hosts.
My script does not take it into account. But it is not difficult to adjust it for a specific situation.
