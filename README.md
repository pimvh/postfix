![Molecule test](https://github.com/pimvh/postfix/actions/workflows/test.yaml/badge.svg)
![Molecule test](https://github.com/pimvh/postfix/actions/workflowss/test.yaml/badge.svg)

# Requirements

1. Ansible installed:

```
sudo apt install python3
python3 -m ensurepip --upgrade
pip3 install ansible
```

2. This role installed:

```
ansible-galaxy install pimvh.postfix
```

## Required variables

Review the variables as shown in defaults. A description of what the variables entail is given in the argument spec, in meta/main.yaml. The variables passed to this role are validated by the argument spec at runtime.

# Example playbook

A simple way to run this role on a host, is the following:

```
- hosts:
  - foo

  vars:
    postfix_ipv4: << Pass the IPv4 address of the postfix mail server here >>
    postfix_ipv6: << Pass the IPv6 address of the Postfix mail server here >>
    postfix_myhostname: "<< Pass the postfix domain name here >>"
    postfix_mydomain: "<< Pass the postfix domain here, defaults to myhostname >>"
    postfix_mynetworks:
      - 127.0.0.0/8
      - "[::1]/128"
    # Add additional networks when required
    postfix_virtual_alias_domains: [] # Add virtual aliases domains when required (see meta/main.yaml for structure)
    postfix_relay_domains: [] # Add relay domains when required (see defaults/main.yaml for structure)
    postfix_aliases: # Add user aliases when required
      - user: root
        alias: postmaster
    # can be also a list of users
    # - users:
    #     - fred
    #     - foo
    #     - bar
    #   alias: something

    postfix_virtual_aliases: [] # Add virtual aliases when required (see meta/main.yaml for structure)

    # You probably can skip these rest of the variables
    # postfix_install: true
    # postfix_dir: /etc/postfix

    # postfix_dkim_enabled: true # DKIM is by default enabled
    # postfix_dkim_keys:
    #   default:
    #     mail: "*"

    # DKIM file placement the filesystem
    # postfix_dkim_keytable: /etc/opendkim/keytable
    # postfix_dkim_signingtable: /etc/opendkim/signingtable
    # postfix_dkim_trustedhosts: "/etc/opendkim/trustedhosts"

    # cert location is based on certbots default place (you can run the role pimvh.certbot to pull certs)
    # postfix_smtpd_tls_cert_file: "/etc/letsencrypt/live/{{ postfix_mydomain }}/fullchain.pem"
    # postfix_smtpd_tls_key_file: "/etc/letsencrypt/live/{{ postfix_mydomain }}/privkey.pem"

  roles:
    - pimvh.postfix

```

You will probably save yourself some refactors if do not set variables inline, but based on hosts and/or groups. However, this depends on your specific use-case. Take a look at the Ansible recommended playbook setup for this.

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

I haven't gotten around to configuring the setup of a database as a back-end for postfix. If you're interested, feel free to contribute.

# Troubleshooting

This role validates the passed variables. If you:

- see issues with the argument spec, you probably made an error when passing variables to this role.
- encounter problems while running this playbook, don't hesitate to describe your issue in details and open an issue.

# Future Improvements

There are still a number of things which can be improved for this role. The following things are things I am considering of adding:

- Finish implementing opendmarc dashboard
- Add a better backend to the postfix server, like a database instead of the bare filesystem.

If you have other Improvements, feel free to open an issue.

# Sources

- [Postfix documentation](https://www.postfix.org/documentation.html)
- [SIDN guide on configuring Postfix](https://www.sidn.nl/en/news-and-blogs/hands-on-implementing-spf-dkim-and-dmarc-in-postfix)
- [How to configure Dovecot](https://www.linuxbabe.com/mail-server/install-dovecot-imap-server-debian)
- [Dovecot installation test commands](https://wiki2.dovecot.org/TestInstallation)
