# owlEye-text-server
A demo of text server working with [owlEye](https://github.com/JerryLiao26/owlEye)

## Requirements
This demo use ```pipenv``` to manage dependencies. Install it with:
```
pip3 install pipenv
```

## APIs
To be able to run with ```owlEye```, your server should also have following APIs:
- /hello
  - Method: GET
  - Response:
  ```json
  {
      "status": true
  }
  ```
