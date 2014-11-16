[Pixel & Kraft](http://pixelandkraft.com)
#Adapto Theme <br><small>Master Documentation</small>

**First off,** many thanks for purchasing Adapto. We hope you enjoy using it as much as we enjoyed crafting it.

###Always updated
This document is the master documentation. If you're reading it from your downloaded zip of Adapto, we recommend [visiting it online](https://drive.google.com/file/d/0B_eAxsmtYtbeOG4wT1BCTUZfU3M/edit?usp=sharing) to bookmark and reference the "always up to date" version. 

---
## Master Table of Contents

- [Getting Started](#getting-started)
- [Methods of Customization](#methods-of-customization)
- [Adapto Docs](#adapto-docs)

---

## Getting Started

Adapto is ready to go out of the box. Inside your zip file, you'll see a theme folder. To view these files on your computer, unzip them and open up any of the html files. From there, you can navigate around Adapto, just as you can on the [live Adapto demo](http://pixelandkraft.com/adapto/demo). 

But it's likely that you'll want to customize Adapto for your particular needs.. after all, this is *Adapto,* right?

## What you Need
Only one thing is needed for adapting Adapto: A text editor. If you've worked with code before, you likely already have one setup. If not, you'll need to download one. But first, what is a text editor? Simply put, it's a program for editing code. It's different than a program like Microsoft's Word (never *ever* use Word to edit code). 

**Getting a text editor**
The good news is that even the best text editors can be had for free (even if via never-ending trials). Such is the case with my prefered one: Sublime Text. 
Download sublime text here: http://www.sublimetext.com/3
Checkout these awesome tutorials on getting the most out of it: http://code.tutsplus.com/articles/perfect-workflow-in-sublime-text-free-course--net-27293

>Note: Sublime Text 3 is techincally stll in beta, but it's fully functional (and quite an improvement over Sublime text 2 - though it was always pretty incredible. Regardless, if you have trouble with it, or just want to play it extra safe, go with Sublime Text 2, found here: http://www.sublimetext.com/2 )

**Other worthy text editors to consider:**
[Atom Editor](https://atom.io/) - From the folks at GitHub, currently only on IOs (though Windows and Linux versions coming soon).
[Notepad++](http://notepad-plus-plus.org/) - A sweet little application, though not nearly as powerful as the above.

---
## Methods of Customization
Ease of customization was a primary focus throughout the architecture and building of Adapto (to keep it as *adaptable* as possible). For style customizations, there are two primary approaches:

1. Work with straight CSS
2. Work with Sass (a CSS preprocessor)

**1. Plain CSS**
Not much to say here. The plain CSS is there, ready to be customized by those not wanting to use Sass... but *do* please do yourself the favor and *at least consider* the Sass route. It's not hard, not even a little, and it really does add super powers to your styling abilities. 
>Your time and energy will go *much* further if you customize with Sass.

**2. Sass**
The importance of utilizing a CSS pre-processor is so great that we've dedicated an entire section to it on the demo. If you haven't yet seen it, or would generally like some pointers on where to look for getting started with Sass, [read the "Built with Sass" section on "What Makes Adapto Different"](http://pixelandkraft.com/adapto/demo/pages/what-makes-adapto-different.html). 

In a nutshell, Sass brings simple yet powerful programming concepts into the world of CSS (such as variables, functions, and logic). Most importantly, to more greatly assist you in efforts to even further adapto Adapto to your needs, *the task is as easy as changing a few variables*. 

It's important to note that Adapto is built with the `.scss` version of Sass. We'd have liked to use the must more elegant `.sass` version, but because it's not currently supported by LibSass we are having to currently develop with the bracketed syntax. 

Work with Sass to fully unlease Adapto's adaptability.
In order to do so, you'll need a way to compile the `.scss` files. 

Here are some options for compiling Sass: 

> All in one Desktop Apps:

>- [Prepos](http://alphapixels.com/prepros/) (cross platform, free)
- [Mixture](http://mixture.io/) (cross platform, paid)
- [Code Kit](https://incident57.com/codekit/) (mac only, paid)
- [hammer](http://hammerformac.com/) (mac only, paid)

> Command Line Approaches

>- [Grunt](http://gruntjs.com/)
- [Gulp](http://gulpjs.com/)
- many others (if you're comfortable with the command line you likely already know how to compile Sass)

These are each rather powerful applications that will do much more than simply compile your `.scss` files. Check out their feature lists to fully understand. 

>**Important!** 

>However you choose to compile, it's *crucial* that the method include support for [Autoprefixer](https://github.com/ai/autoprefixer).
We've developed Adapto with the aid of Autoprefixer, which means that CSS3 elements don't have their vendor prefixes in the core Adapto code. 

>The good news? Autoprefixer will change your life (in an awesome way) and the above mentioned compiling tools (and others) make it a easy as clicking a button or two (Codekit even auto-prefixes by default, I believe). 



---
## Adapto Docs

#### Contents
- [Stylesheets](#stylesheets) (theme schemes)
- [Images](#images)
- [Background noise](#background-noise)
- [Extra top header](#extra-top-header)
- [Site Layout](#site-layout) (boxed/wide)
- [Top and Bottom Space](#top-and-bottom-space)
- [Boxed BG Color/Pattern/Texture](#Boxed-BG-Color/Pattern/Texture)
- [Icons](#icons)
- [Smooth Scrolling](#smooth-scrolling)

---

### Stylesheets
####(Theme Schemes)

First off, if you're not quite clear on what a stylesheet is, it's simply a file containing code for how the website (theme) looks.

Adapto has been architected to need only one stylesheet.[^fn-stylesheet_qualification] Why? Because, in general terms, the fewer stylesheets a site has the faster it will load (the browser makes a request to the server for *each* stylesheet on the page being loaded, so fewer = faster). 

[^fn-stylesheet_qualification]: Technically, Adapto requires one additional stylesheet for its fonts (from Google). The link to it in the `head` of every html document looks like this (though this is abbreviated): `<link href='http://fonts.googleapis.com...' rel='stylesheet' type='text/css'>`

Adapto comes with 20 predefined stylesheets (10 light and 10 dark). Both minified and unminified versions are supplied and each is available for quick preview in the demo. 

Each Adapto stylesheet has been named in the following manner:
`global-style` + `_light` or `_dark` + `--SCHEME-COLOR-HERE` + `.css`
For minified versions, the above forumla is followed, only the last `.css` is replaced with `.min.css`

Example: The default Adapto theme is `global-style_light--blue.min.css`

>**Recommendation:** Always use minified versions of stylesheets and js files in production. Unminified is generally only for development.

#### **To Activate a Stylesheet:**

1. Decide on which stylesheet you'd like to activate (using the style widget on the [Adapto demo](http://pixelandkraft.com/adapto/demo)).
2. Locate that stylesheet in the css directory (`Adapto Theme -> Assets -> css`)
3. Replace the default `global-style_light--blue.min.css` with the stylesheet of your preferred theme scheme.

Example: I've just bought adapto and want to use the dark purple stylesheet (theme scheme). In the `head` section for each `html` file, I find the line that looks like this: 

    <!-- CORE DEFAULT Stylesheet (theme scheme) - CHANGE THEME SCHEME HERE -->
    <link href="assets/css/global-style_light--blue.min.css" rel="stylesheet" >


and I change it to this: 

    <!-- CORE DEFAULT Stylesheet (theme scheme) - CHANGE THEME SCHEME HERE -->
    <link href="assets/css/global-style_dark--purple.min.css" rel="stylesheet" >

>**Stylesheet naming conventions:**
**In a nutshell:** We've tried to keep stylesheet naming logical and predictable. If a theme scheme in the demo looks purple it's named purple. For colors that have more than one version, a simple `2` or `3` is added to the end of the color name. 


#### **To Edit a Stylesheet:**
Stylesheets can be edited as stright `css` or as `sass` or, technically, `scss`. We *strongly* suggest that you use Sass to make any customizations, as we've done our best to make the task *incredibly* easy by harnessing the power of things like variables and if statements. 

There are two choices to make when editing a stylesheet: `light or dark?` and `which color?`. 

**To edit a light stylesheet,** locate the `_settings-scheme_light.scss` file, found in the `light` stylesheet directory (`source/stylesheets/adapto/dark`).
**To edit a dark stylesheet,** locate the `_settings-scheme_dark.scss` file, found in the `dark` stylesheet directory (`source/stylesheets/adapto/dark`).

Inside both of these files is a detailed table of contents. **The first and most crucial step* is to activate the stylesheet you'd like to edit. This is done in section 1.1, Toggles ---> Stylesheet Compiles. By default, most of these are set to `false`. This keeps the sass from compiling all of the stylesheets on each save (which slows down the compiling process). To edit any of these stylesheets, simply set the desired one to `true`. 

>**Here's an example:**
Say I just bought Adapto and I now want to make some edits to the light brown stylesheet. I'd go into the `_settings-scheme)light.scss` file, locate line 39 that reads `$global-style_light--brown:     false;` and change the `fase` to `true`. 

---

### Images
All images by default have a border applied. If for some reason you'd like an image with no border (say, for a logo) simply wrap it in a `div` with the class of `no-border`. 
Example:

    <div class="no-border">
        <img src="borderless-image.jpg" alt="borderless image">
    </div>

---

### Background Noise

Quickly see if you'd like to apply background noise to different parts of the theme in [the demo](http://pixelandkraft.com/adapto/demo/) (via the adaptation (style) widget).

There are two ways that background noise can be added to pages in Adapto: 
1. [with HTML classes](#html-class-method)
2. [with Sass](#sass-method)

#### HTML Class Method

**Body**

Add the class `bg-noise` to the div with the class of `page-wrap`. Here's the full code:

    <div class="page-wrap bg-noise">

**Nav Header**

Add the class `bg-noise` to the `header` tag *and* and the `nav` tag. Here's the full code:

    <!-- header tag -->
    <header id="header" class="header bg-noise" role="banner">
    
    <!-- nav tag -->
    <nav class="navbar bg-noise" role="navigation">

**Page Header**

Add the class `bg-noise` to the div with the class of `page-header-wrap`. Here's the full code:

    <div class="page-header-wrap bg-noise">

**Footer**

Add the class `bg-noise` to the `footer` tag. Here's the full code:

    <footer class="site-footer footer bg-noise">

    
>**Remember:** The order of class names inside the same div or other tag in HTML is *not* significant.

>**Tip:** This class can be added to virtually any other div or other tag. Feel free to experiment. 

#### Sass Method

Setting background noise with Sass is much more quick and easy than the former html method. Here's how to do it:

1. Decide whether you're using a light or dark color scheme (there's a master `settings` file for each).
2. Locate either the light or dark `settings` file, respectively named `_settings-scheme_light.scss` and `_settings-scheme_dark.scss`.
3. Inside the file, the noise background toggles are the first entry (note master legend).
4. By default, they're `false` which means "off." To toggle "on," change to `true`. 

>**Important:** For this an all other Sass methods, you *must* compile the `.scss` files. 
Need a way to compile? Here are some options: 
- [Prepos](http://alphapixels.com/prepros/) (cross platform, free)
- [Mixture](http://mixture.io/) (cross platform, paid)
- [Code Kit](https://incident57.com/codekit/) (mac only, paid)

---

### Extra Top Header

To activate the extra top header (as found in the demo), follow these steps:

1. **Remove** the class `"header-hidden"` from `<div class="extra-header header-hidden">`.
2. **Add ONE** header-size class to the same div.
    Header-size class options:
    - `header-small`
    - `header-medium`
    - `header-large`
    - `header-xl`

3. Decide which content you'd like in the extra header and customize to meet your needs. Remove the class `"header-hidden"` from each list that you want.

        <div class="extra-header header-hidden">
          <div class="container">
            <ul class="list-inline extra-header-store header-hidden">
              <li><a href="#"><span class="ai ai-cart"></span> Cart | 2 items</a></li>
              <li><a href="#"><span class="ai ai-coin"></span> Checkout</a></li>
            </ul>
            <ul class="list-inline extra-header-account header-hidden">
              <li><a href="#"><span class="ai ai-question"></span> HELP</a></li>
              | <li><a href="#"><span class="ai ai-user3"></span> LOGIN</a></li>
            </ul>
            <ul class="list-inline extra-header-socialMedia-2 header-hidden">
              <li><a href="#"><span class="ai ai-linkedin"></span></a></li>
              <li><a href="#"><span class="ai ai-picassa2"></span></a></li>
              <li><a href="#"><span class="ai ai-soundcloud2"></span></a></li>
            </ul>
            <ul class="list-inline extra-header-socialMedia extra-header-default-content">
              <li><a href="#"><span class="ai ai-facebook2"></span></a></li>
              <li><a href="#"><span class="ai ai-twitter2"></span></a></li>
              <li><a href="#"><span class="ai ai-google-plus3"></span></a></li>
            </ul>
            <ul class="list-inline extra-header-phone extra-header-default-content">
              <li><span class="ai ai-phone"></span> <a href="tel:+18007772323">(1800) 777-2323</a></li>
            </ul>
          </div>
        </div>


---

### Site Layout

By default, Adapto is full width. If you'd like to make the header, body, and/or footer boxed (as possible via the widget in the demo), follow these steps:

#### **Header**

**For the default navbar/header**
    1. Locate the site header tag with a class of header
    2. Add the class `boxed`
    
Example:

 1. Locate this: 
 `<header id="header" class="header slide animated headroom--top boxed" role="banner">`
 2. Add this: 
 `boxed`
 3. So it looks like this: 
 `<header id="header" class="boxed header slide animated headroom--top boxed" role="banner">`

*Note: the order of HTML classes is not important.*
   
**For the extra header**
    1. Locate the div with a class of `extra-header`
    2. Add the class `boxed`

Example: 

1. Locate this: 
`<div class="extra-header header-small">...</div>`
2. Add this: 
`boxed`
3. So it looks like this:
`<div class="boxed extra-header header-small">...</div>`


#### **Body**
1. Find the div with a class of `page-wrap`
2. Add `boxed`

(so it looks like this: `<div class="page-wrap boxed">`)

#### **Footer**
1. Find the footer tag that looks like this `<footer class="site-footer footer">`
2. Add the class `boxed`

(so it looks like this: `<footer class="site-footer footer boxed">`)

---
### Top and Bottom Space
By default, Adapto has no top or bottom space between the site container and the browser. To add top/bottom space as seen possible in the demo, follow these steps: 

**To Add Top Space:**
1. Find the body tag (`<body id="top">`)
2. Add the class `body-space-top`
(so it looks like: `<body id="top" class="body-space-top">`)

**To Add Bottom Space:**
1. Find the body tag (`<body id="top">`)
2. Add the class `body-space-bottom`
(so it looks like: `<body id="top" class="body-space-bottom">`)

**To Add Top & Bottom Space:**
1. Find the body tag.
2. Add both of the above classes.
(so it looks like: `<body id="top" class="body-space-top body-space-bottom">`)

---

### Boxed BG Color/Pattern/Texture
If you're using Adapto in its boxed form and would like to change the background color or add a pattern or texture, follow these steps:

1. Find the body tag (`<body id="top">`)
2. Add the desired background color class and/or background pattern class. 

**BG Color Classes**
Background color classes follow this formula: 

> `bg-` + `name of color`

Here's how to know the name of your desired color, based on the widget in the demo: 

The first Boxed BG Color is always the color that's selected as the "theme scheme." The class for this color is `brand-color`. 
If you wanted to use this, your body tag would look something like this: 
`<body id="top" class="bg-brand-color">`

The rest, in order of left to right:
`white`
`gray-lighter`
`gray-light`
`gray`
`gray-dark`
`gray-darker`
`black`
`blue`
`brown`

So to use any of these as the background color, simply combine it with the text `bg-` to form the proper background color class, then add that to the body tag. 

>Example: `<body id="top" class="bg-gray-lighter">`


**BG Pattern/Texture Classes:**
These are easy, they follow this formula: 

>`bg-pattern` + `1` or `2` or `3`, etc.

To know the number of your desired pattern/texture, simply count! They're in sequential order on the demo (and the white x for no patter/texture does NOT count). 

>**For example:** Say you want to add noise to your boxed bg, then your body tag would look something like this: 
`<body id="top" class="bg-pattern-5">`

<br>

>**Tip:** Background colors and texture/patterns can be combined! (you may have noticed this in the demo).
**Example:** 
`<body id="top" class="bg-pattern-5 bg-gray-darker">`


---

### Icons

Adpto has a full set of icon fonts ready for use in your project. The set is a custom selection of free fonts offered by the the wonderful [Icon Moon](http://icomoon.io/) app. 

To use an icon, there are essentially two steps:

1. Decide on the best icon to use.
2. Add necessary classes and markup to the HTML.

**For the first step,** simply use the icon section of the Adapto demo to quickly find the right icon. 
**For the second,** click on the icon and copy the pre-selected class names. 

A minimum of two class names are needed to use an icon: `ai` and `ai-ICON-NAME-HERE`. These are what the demo give you when clicking on an icon. Then, in your html, include the following markup.

    <i class="ai ai-home"></i>
    
In case it's not obvious, this code displays an icon of a house.
    
For fancier code and usage examples (such as spinning, in-circled, in-listed, flied, and rotated), visit the [icon example section](http://pixelandkraft.com/adapto/demo/elements.html#elements-icons-examples) of the demo.

---

### Smooth Scrolling

To create in-page links that smoothly scroll to an area of the page (anchor links), follow this simple formula: 

**Add to the link**
`href="#destination"` + `data-toggle="smoothScroll"`

**Add to the destination**
`id="destination"`

Here's an example of a link that would smoothly scroll to the top of the page.

Link

    <a href="#top" data-toggle="smoothScroll">Go to Top</a>

Destination

    <div id="top"></div>

<small>note: for this to work, this div with an id of `top` would be located at the top of the page.</small>


---
#Footnotes



