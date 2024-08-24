#!/usr/bin/env bash
# Setting up my client configuration file

file { 'ect/ssh/ssh_config':
  	ensure => present,
content =>"

	#client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
}
