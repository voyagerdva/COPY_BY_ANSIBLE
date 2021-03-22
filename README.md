Task:
If you want to upload some file once per hour to 1 server from 1000 servers, how it can be done? What special cases should be taken into account?

We can use ansible for upload each hour to 1 of 1000s servers .

We might run related playbook by using script, which
    -   counts index. It means steps from zero up to max_servers and from zero again (it changes index each time/hour);
    -   finds to the current server’s address according to index;
    -   constructs new inventory file according to the address of the desired host;
    -   runs ansible playbook;
    -   writes result to file Hosts_DONE.txt;
    -   changes index to next (or to zero if index reached server’s maximum).


We need to configure the crontab according to these settings (for run it automatically hour by hour):
    0 */1 * * * cd <SCRIPT_DIR>/ && ./run_copy.py

Special cases are associated with the violation of ssh key fingerprints and with usernames and passwords on servers

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
