# Requirements

1. Ansible installed:

```
sudo apt install python3
python3 -m ensurepip --upgrade
pip3 install ansible
```

## Required variables

Review the variables as shown in defaults.

# Example playbook

```
hosts:
  - foo
roles:
  - pimvh.postfix

```

Note that this role is dependant on pimvh.certbot, for its TLS certificate.

You probably want to pass certbot related variables as well, which can be found [here](https://github.com/pimvh/certbot).

# TLDR - What will happen if I run this

- validate whether variables are all right
- install postfix
- install and configure amavis
- install and configure opendkim
- install and configure opendmarc
- install and configure dovecot with system-users being able to login and receive mail
- configure mailutils (installed by role this is dependant on)
- install and configure opendmarc dashboard (WIP)

# Future Improvements

- Finish implementing opendmarc dashboard
- Add alternatives to certbot role

# Sources

- [Postfix documentation](https://www.postfix.org/documentation.html)
- [SIDN guide on configuring Postfix](https://www.sidn.nl/en/news-and-blogs/hands-on-implementing-spf-dkim-and-dmarc-in-postfix)
- [How to configure Dovecot](https://www.linuxbabe.com/mail-server/install-dovecot-imap-server-debian)
- [Dovecot installation test commands](https://wiki2.dovecot.org/TestInstallation)
