# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Esta linea permite que todos los nodos definidos en este 'Vagrantfile' 
  # instalen 'docker' y 'docker-compose'
  config.vm.provision "shell", path: "install_docker_tools.sh"
  config.vm.provision "shell", inline: "cat /vagrant/hosts >> /etc/hosts"
  config.vm.box = "ubuntu/bionic64"
  config.vm.define "manager" do |swarm|
  	swarm.vm.hostname = "manager"
	  swarm.vm.network "private_network", ip: "192.168.33.10"
    swarm.vm.provision "shell" do |s| 
      s.path = "setup_swarm.sh"
      s.args = ["manager"]
    end
  	swarm.vm.provider :virtualbox do |vb|
		  vb.customize [ 'modifyvm', :id, '--memory', '1024' ]
		  vb.customize [ 'modifyvm', :id, '--cpus', '2' ]
		  vb.customize [ 'modifyvm', :id, '--name', 'swarm-manager' ]
  	end
  end
  config.vm.define "worker-01" do |swarm1|
  	swarm1.vm.hostname = "worker-01"
	  swarm1.vm.network "private_network", ip: "192.168.33.11"
    swarm1.vm.provision "shell" do |s1| 
      s1.path = "setup_swarm.sh"
      s1.args = ["worker-01"]
    end
  	swarm1.vm.provider :virtualbox do |vb1|
		  vb1.customize [ 'modifyvm', :id, '--memory', '1024' ]
		  vb1.customize [ 'modifyvm', :id, '--cpus', '2' ]
		  vb1.customize [ 'modifyvm', :id, '--name', 'worker-01' ]
  	end
  end
  config.vm.define "worker-02" do |swarm2|
    swarm2.vm.hostname = "worker-02"
	  swarm2.vm.network "private_network", ip: "192.168.33.12"
    swarm2.vm.provision "shell" do |s2| 
      s2.path = "setup_swarm.sh"
      s2.args = ["worker-02"]
    end
  	swarm2.vm.provider :virtualbox do |vb2|
		  vb2.customize [ 'modifyvm', :id, '--memory', '1024' ]
		  vb2.customize [ 'modifyvm', :id, '--cpus', '2' ]
		  vb2.customize [ 'modifyvm', :id, '--name', 'worker-02' ]
  	end
  end
end
