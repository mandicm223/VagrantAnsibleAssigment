# Vagrantfile

VAGRANTFILE_API_VERSION = "2"

# Configuration Variables
BOX_NAME = "ubuntu/jammy64"
FIXED_IP = "192.168.50.4"
VM_MEMORY = 2048   # 2GB RAM
VM_CPUS = 2        # 2 CPUs

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = BOX_NAME

  # Configure VM network with a fixed IP
  config.vm.network "private_network", ip: FIXED_IP, auto_config: true, type: "static"
  
  # Set resources
  config.vm.provider "virtualbox" do |vb|
    vb.name = "ubuntu-dev-vm"
    vb.memory = VM_MEMORY
    vb.cpus = VM_CPUS
    vb.customize ["createhd", "--filename", "disk_#{Time.now.to_i}.vdi", "--size", 10240]
  end

  # Provisioning with Ansible
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/playbook.yml"
    ansible.inventory_path = "ansible/inventory.ini"
  end
end
