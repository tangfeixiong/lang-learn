
## Run anaconda3

rasp@test-02:~/llm-workspace$ docker run -ti -p 8888:8888 -v `pwd`:/home --name anaconda3 continuumio/anaconda3

### Local config (Optional)

__Modify deb package mirror__

(base) root@aaa42471b88f:/home# sed -i.bak "s%http://deb.debian.org%https://repo.huaweicloud.com%g" /etc/apt/sources.list

(base) root@aaa42471b88f:/home# apt-get install apt-transport-https ca-certificates

(base) root@aaa42471b88f:/home# apt-get update

__Config pypi mirror__

(base) root@aaa42471b88f:/# pip config --user set global.extra-index-url "https://repo.huaweicloud.com/repository/pypi/simple https://pypi.tuna.tsinghua.edu.cn/simple https://mirrors.aliyun.com/pypi/simple https://download.pytorch.org/whl/cpu"

(base) root@aaa42471b88f:/# pip config --user set glbal.timeout 120

### Jupyter workplace

__FLAN-T5__

Reference
  + [Running the Large Language Model FLAN-T5 locally](https://heidloff.net/article/running-llm-flan-t5-locally/)

(base) root@aaa42471b88f:/# python -m venv /home/venv

(base) root@aaa42471b88f:/# source /home/venv/bin/activate

(base) root@aaa42471b88f:/# pip install --root-user-action=ignore transformers

(base) root@aaa42471b88f:/# pip install --root-user-action=ignore transformers[torch]

(base) root@aaa42471b88f:/# pip3 install --root-user-action=ignore torch torchvision torchaudio

(base) root@aaa42471b88f:/# conda install pytorch torchvision torchaudio cpuonly -c pytorch

(base) root@aaa42471b88f:/# jupyter lab --ip='0.0.0.0' --port=8888 --no-browser --allow-root --notebook-dir=/home

__BLOOM__

Reference
  + [Some quick BLOOM LLM examples](https://github.com/Sentdex/BLOOM_Examples)
    


