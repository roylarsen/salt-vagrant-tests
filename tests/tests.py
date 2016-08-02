def test_test_file(File):
  test_file = File("/home/vagrant/test.txt")
  assert test_file.contains("This is")
  assert test_file.user == "root"
  assert test_file.group == "root"
