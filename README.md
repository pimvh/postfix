# Requirements

1. Ansible installed:

```
sudo apt install python3
python3 -m ensurepip --upgrade
pip3 install ansible
```

## Required variables

Review the variables as shown in defaults. A description of what the variables entail is given in the argument spec, in meta/main.yaml.

You probably want to pass certbot related variables as well, which can be found [here](https://github.com/pimvh/certbot).

# Example playbook

```
hosts:
  - foo

roles:
  - pimvh.postfix

```

Note that this role is dependant on pimvh.certbot, for getting a TLS certificate.

# TLDR - What will happen if I run this

- validate whether variables are all right
- install postfix
- install and configure amavis
- install and configure opendkim
- install and configure opendmarc
- install and configure dovecot with system-users being able to login and receive mail
- configure mailutils (installed by role this is dependant on)
- install and configure opendmarc dashboard (WIP)

# What this role does not do

## Firewalling

This role does not do any firewalling, due to you probably having specific requirements for that. You probably do not want to open your IMAP port to the entire internet, if you can avoid it. So take care!

## Setting up a database backend

I haven't gotten around to configuring the setup of a database as a backend for postfix. If you're interested, feel free to contribute.

# Future Improvements

- Finish implementing opendmarc dashboard
- Add alternatives to certbot role

# Sources

- [Postfix documentation](https://www.postfix.org/documentation.html)
- [SIDN guide on configuring Postfix](https://www.sidn.nl/en/news-and-blogs/hands-on-implementing-spf-dkim-and-dmarc-in-postfix)
- [How to configure Dovecot](https://www.linuxbabe.com/mail-server/install-dovecot-imap-server-debian)
- [Dovecot installation test commands](https://wiki2.dovecot.org/TestInstallation)
