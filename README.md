# sickninja
Stylesheet generator that uses sass and jinja2

## Dependencies @archlinux
* python-jinja
* ruby-sass
* inotify-tools

## Usage
#### Arguments
`sickninja infile outfile style watchdir`
#### Direct
`sickninja style.ninja style.css compressed`
#### Watch current directory
`sickninja style.ninja style.css compressed .`

### Example
***generic.ninja***
```
body {
  # block body
  color: #FFF;
  # endblock
}
```
***special.ninja***
```
# extends 'generic.ninja'
# block body
color: #000;
# endblock
```

`> sickninja special.ninja special.css compressed`

***special.css***
```
body{color:#000}
```
