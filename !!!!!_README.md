
Explanation:

For upload each hour to 1 of 1000s servers we can use ad-hoc command of ansible 
# ansible all -m copy -a "src=<our_file> dest=<dest_dir> " -b

We might run it from script, which
-	counts steps from zero to max_servers and from zero again (it changes index each time/hour);
-	looks to the current server’s number according to index;
-	constructs new inventory file according to the address of the desired host;
-	runs ansible command (look upper);
-	writes result to file Hosts_DONE.txt;
-	changes index to next (or to zero if index reached server’s maximum).
We need to configure the crontab according to these settings (for run it automatically hour by hour):

    0 */1 * * * cd <SCRIPT_DIR>/ && ./run_copy.py

We can use scp command instead of ansible. Then it need to change the code in the script a little. 
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

scp -o "UserKnownHostsFile=/dev/null" -o "StrictHostKeyChecking=no" <file> user@host:/<dir>

(if we use scp)

Or 
host_key_checking = False in ./ansible.cfg

if we use ansible.

we also need to pay attention to the users, passwords, and access rights on the target hosts.
My script does not take it into account. But it is not difficult to adjust it for a specific situation.
