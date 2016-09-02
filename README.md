#Graphite cluster

Setup redundant carbon cache and graphite web

#Role variables

- number of caches per host `carbon_caches`. one per cpu is a good start
- hosts of this group are used for configuration `graphite_groupname`
- configure apache on this port `graphite_apache_port`
- add data redundancy `graphite_replication_factor`

##Database setup

@see graphitedb_* vars in main.yml

The database must exists. This role does NOT create it for you

To stay clustered maybe have a look at : [galera-cluster](https://github.com/netzwirt/ansible-galera-cluster)

#Example Playbook

    - hosts: graphite
      become: True
      roles:
         - netzwirt.graphite-cluster

# License

BSD

# Author Information

[netzwirt](https://github.com/netzwirt)