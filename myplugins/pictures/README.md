# Responsive Image Processing

## Procedure

- To avoid high res images being copied to content, place them in a directory not registered as a static paths directory


- Parse html generated from markdown to search for img tags using BeautifulSoup
- Add srcset attribute to tag
  - widths come from list in settings
  - write out srcset attribute by looping through list
- hash each source image, save resized images as per their hash

##  ToDo

- Prevent deletion when output is cleared on reload
- move images to seperate url such as s3
- Retina??
