
# coding: utf-8

# In[ ]:


import subprocess, shlex
cmd = shlex.split("/home/pi/dw1000_rpi_new/src/dw1000_tx")
print(subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode("utf-8"))

