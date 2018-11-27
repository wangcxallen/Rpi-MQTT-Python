
# coding: utf-8

# In[ ]:


import subprocess, shlex
cmd = shlex.split("/home/pi/dw1000_rpi_new/src/dw1000_tx")
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
print(p.communicate()[0].decode("utf-8"))
