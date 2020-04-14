..  {{ cookiecutter.project_name }} master file

    Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
    Licensed according to the regulations of {{ cookiecutter.license }}.

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#############################################################################
{{ cookiecutter.document_title }}
#############################################################################

This is a `Sphinx document`_ that will contain something you want to write about.

{{ cookiecutter.short_description }}

.. _`Sphinx document`: https://github.com/Springerle/sphinx-document#readme


************
Introduction
************

...


**************
Adding Visuals
**************

Embedding Graphs
================

The `sphinx.ext.graphviz extension`_ allows you to directly embed GraphViz
‘dot language’ graphs into your document files.
They are then rendered to PNG or SVG images, which get added to the generated HTML documentation.

Using SVG (set as the default in ``conf.py``) allows you to hot-link your nodes to any HTTP resource.
As long as nodes have a ``href`` attribute, the SVG rendering contains them
and thus node labels become clickable hyperlinks -- try it out below.

.. graphviz::
    :name: sphinx.ext.graphviz
    :caption: Sphinx and GraphViz Data Flow
    :alt: How Sphinx and GraphViz Render the Final Document
    :align: center

     digraph "sphinx-ext-graphviz" {
         size="6,4";
         rankdir="LR";
         graph [fontname="Verdana", fontsize="12"];
         node [fontname="Verdana", fontsize="12"];
         edge [fontname="Sans", fontsize="9"];

         sphinx [label="Sphinx", shape="component",
                 href="https://www.sphinx-doc.org/",
                 target="_blank"];
         dot [label="GraphViz", shape="component",
              href="https://www.graphviz.org/",
              target="_blank"];
         docs [label="Docs (.rst)", shape="folder",
               fillcolor="#33ff33", style=filled];
         svg_file [label="SVG Image", shape="note", fontcolor=white,
                   fillcolor="#3333ff", style=filled];
         html_files [label="HTML Files", shape="folder",
                     fillcolor=yellow, style=filled];

         docs -> sphinx [label=" parse "];
         sphinx -> dot [label=" call ", style=dashed, arrowhead=none];
         dot -> svg_file [label=" draw "];
         sphinx -> html_files [label=" render "];
         svg_file -> html_files [style=dashed];
     }


.. _`sphinx.ext.graphviz extension`: https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html
