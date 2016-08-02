/home/vagrant/test.txt:
  file.managed:
    - source: salt://test/files/test.txt
    - user: root
    - group: root
    - mode: 0777
