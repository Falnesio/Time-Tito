# Gitbook Custom Image Div Plugin

This plugin can display elements in the *div* correctly in HTML. 

```
<div class="image">
  <img src="/assets/image-url.jpg" alt="Alt Text" />
</div>
```

## Usage

### Installation

Add the plugin to your `book.json`:

```
{
    "plugins" : [ "image-div" ]
}
```

### Add Images

For example, add images normally to your document using Markdown

```
<div class="image">
  ![image](/assets/image.jpg)
</div>
```

Each image will be wrapped in a div like this

```
<div class="image">
	<img src="/assets/image.jpg" alt="image" />
</div>
```

### Style It

Add the following CSS to your book to center your images and add some additional spacing:

```
div.image {
	text-align: center;
	padding: 15px 0px;
}
```
