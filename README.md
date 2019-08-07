- Procedure 
1) Clone the repo
```bash
git clone https://github.com/raghavendra1806/companyName.git
```
2) Build image using Dockerfile
```bash
cd companyName
docker build -t companyName:public .
```

3) create docker container with image id from above
```bash
docker run -it <image id>
```
4) execute below inside the container

```bash
python3 companyName.py <MAC ADDRESS>
