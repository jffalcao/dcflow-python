# Developing in containers

## References

- https://github.com/marcel-dempers/docker-development-youtube-series/
- 


## Code v0 - setup Container

```bash
    docker-compose up
    docker-compose exec devcontainer bash
    git init
    git config --global user.name "Jose Fernando Falcao"
    git config --global user.email "3720255+jffalcao@users.noreply.github.com"
    git tag
    git tag v0 -m "Setup Dev Container"
```

## Code v1 - The mega Flask Tutorial

```bash
# create the projet https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

  python3 -m venv venv
source venv/bin/activate
pip install flask
export FLASK_APP=microblog.py
flask run -h 0.0.0 -p 5000
curl http://localhost:5000

# In a browser navigate to http://localhost:5001
```