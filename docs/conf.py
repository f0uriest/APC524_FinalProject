# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sys
import os
sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath('../'))

# -- Project information -----------------------------------------------------

project = 'GASTOp'
copyright = '2018, Rory Conlin, Paul Kaneelil, Cristian Lacey, Susan Redmond, Dan Shaw, Amlan Sinha'
author = 'Rory Conlin, Paul Kaneelil, Cristian Lacey, Susan Redmond, Dan Shaw, Amlan Sinha'

# The short X.Y version
version = '1.0.1'
# The full version, including alpha/beta/rc tags
release = 'Release Version'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    #    'sphinx_selective_exclude.eager_only',
    #    'sphinx_selective_exclude.search_auto_exclude',
    #    'sphinx_selective_exclude.modindex_exclude',
]

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.md': 'markdown',
# }
# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    #    'canonical_url': '',
    #    'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'both',
    'style_external_links': False,
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = "demo/static/logo-wordmark-light.svg"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'gastopdoc'


# -- Options for LaTeX output ------------------------------------------------

# -- Options for LaTeX output ---------------------------------------------
latex_engine = 'pdflatex'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'letterpaper',

    'fncychap': '\\usepackage{fncychap}',
    'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',
    'figure_align': 'htbp',
    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''
    %% %% %% %% %% %% %% %% %% %% Meher %% %% %% %% %% %% %% %% %%
    %% %add number to subsubsection 2=subsection, 3=subsubsection
    %% % below subsubsection is not good idea.
    \setcounter{secnumdepth}{3}

    %% %% Table of content upto 2=subsection, 3=subsubsection
    \setcounter{tocdepth}{3}

    \usepackage{amsmath,amsfonts,amssymb,amsthm}
    \usepackage{graphicx}
    
    %% % reduce spaces for Table of contents, figures and tables
    %% % it is used "\addtocontents{toc}{\vskip -1.2cm}" etc. in the document
    \usepackage[notlot,nottoc,notlof]{}
    
    \usepackage{color}
    \usepackage{transparent}
    \usepackage{eso-pic}
    \usepackage{lipsum}
    \usepackage{hyperref}
    \usepackage{footnotebackref} %% link at the footnote to go to the place of footnote in the text

    %% spacing between line
    \usepackage{setspace}
    %% %% \onehalfspacing
    %% %% \doublespacing
    \singlespacing
    %% %% %% %% %% % datetime
    \usepackage{datetime}

    %% RO, LE will not work for 'oneside' layout.
    %% Change oneside to twoside in document class
    \usepackage{fancyhdr}
    \pagestyle{fancy}
    \fancyhf{}
    %% % Alternating Header for oneside
    \fancyhead[L]{\ifthenelse{\isodd{\value{page}}}{ \small \nouppercase{\leftmark} }{}}
    \fancyhead[R]{\ifthenelse{\isodd{\value{page}}}{}{ \small \nouppercase{\rightmark} }}
    %% % Alternating Header for two side
    %\fancyhead[RO]{\small \nouppercase{\rightmark}}
    %\fancyhead[LE]{\small \nouppercase{\leftmark}}
    %% for oneside: change footer at right side. If you want to use Left and right then use same as header defined above.
    %% % Alternating Footer for two side
    %\fancyfoot[RO, RE]{\scriptsize Meher Krishna Patel (mekrip@gmail.com)}
    %% % page number
    \fancyfoot[CO, CE]{\thepage}
    \renewcommand{\headrulewidth}{0.5pt}
    \renewcommand{\footrulewidth}{0.5pt}
    %\RequirePackage{tocbibind} %%% comment this to remove page number for following
    \addto\captionsenglish{\renewcommand{\contentsname}{Table of contents}}
    %\addto\captionsenglish{\renewcommand{\listfigurename}{List of figures}}
    %\addto\captionsenglish{\renewcommand{\listtablename}{List of tables}}
     \addto\captionsenglish{\renewcommand{\chaptername}{Chapter}}
    %% reduce spacing for itemize
    \usepackage{enumitem}
    \setlist{nosep}
    %% %% %% %% %% % Quote Styles at the top of chapter
    \usepackage{epigraph}
    \setlength{\epigraphwidth}{0.8\columnwidth}
    \newcommand{\chapterquote}[2]{\epigraphhead[60]{\epigraph{\textit{#1}}{\textbf {\textit{--#2}}}}}
    %% %% %% %% %% % Quote for all places except Chapter
    \newcommand{\sectionquote}[2]{{\quote{\textit{``#1''}}{\textbf {\textit{--#2}}}}}
    ''',

    'maketitle': r'''
    \pagenumbering{Roman} %% % to avoid page 1 conflict with actual page 1
    \begin{titlepage}
    
        \vspace*{80mm} %% % * is used to give space from top
    
        \centering
        \textbf{\Huge {GASTOp Documentation}}
            
        \vspace*{2mm}
        
        \begin{figure}[!h]
        \centering
        \includegraphics[scale=0.3]{images/logo.jpg}
        \end{figure}
            
        \vspace*{10mm}
        
        \centering
        \textbf{ \Large {Rory Conlin, Paul Kaneelil, Cristian Lacey, Susan Redmond,}}
        
        \vspace{1mm}
        
        \centering
        \textbf{ \Large {Dan Shaw, Amlan Sinha}}
            
        \vspace*{10mm}
        
        \centering
        \small {Created: \today}
        %% \vfill adds at the bottom
        
        \vfill
        
    \end{titlepage}
    \clearpage
    %\pagenumbering{roman}
    %\sphinxtableofcontents
    %\clearpage
    \pagenumbering{arabic}
    ''',

    'sphinxsetup': \
    'hmargin={0.7in,0.7in}, vmargin={1in,1in}, \
    verbatimwithframe=true, \
    TitleColor={rgb}{0,0,0}, \
    HeaderFamily=\\rmfamily\\bfseries, \
    InnerLinkColor={rgb}{0,0,1}, \
    OuterLinkColor={rgb}{0,0,1}',

    #   'tableofcontents': '',

}
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'gastop.tex', 'GASTOp Documentation',
     'Rory Conlin, Paul Kaneelil, Cristian Lacey, Susan Redmond, Dan Shaw, Amlan Sinha', 'report', True),
]

latex_toplevel_sectioning = 'chapter'

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'gastop', 'gastop Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'gastop', 'gastop Documentation',
     author, 'gastop', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------
