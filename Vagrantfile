Vagrant.configure("2") do |config|
  config.vm.box = "bento/centos-7.1"
  config.ssh.insert_key = false

  config.vm.synced_folder "test", "/srv/salt"

  config.vm.provision :salt do |salt|
    salt.masterless = true
    salt.minion_config = "salt/minion"
    salt.run_highstate = true
  end
end
