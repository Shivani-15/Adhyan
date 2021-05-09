# Adhyan
### A web app for online group studies.

**To install latest version of channels:** <br>
 git clone git@github.com:django/channels.git <br>
 cd channels <br>
 <activate your project’s virtual environment> <br>
 (environment) pip3 install -e .  

**To install docker:**

Follow this: (https://docs.docker.com/engine/install/)

or

sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get update

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
 sudo apt-get update

 sudo apt-get install docker-ce docker-ce-cli containerd.io
 sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io
 
 
**Tu run the file:**

docker run -p 6379:6379 -d redis:5
python3 manage.py runserver
