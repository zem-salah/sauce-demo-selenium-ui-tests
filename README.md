# Sauce lab UI automation demo

The goal of this repo is to act as a portfolio showing UI automation skills using selenium.

The idea is to have a framework that is readable and maintainable using patterns like POM (page object model), factory and composition.

## Prerequisites

- Python 3.8
- a virtual env manager

## Installation

1. Clone the repository
2. Create and activate a virtual env
3. Install required packages

```bash
    pip install .
```

## Run tests

```bash
    behave
```

## Repo organisation

Here I present the modules present in the repo and their purpose :

`components`: used to store parts of pages that will be used to interact with 
a whole page. For example, product page is composed of 2 headers, a main 
content and a footer.

`data`: contain classes that will be used to get test datas through a 
friendly API

`features`: specific to behave framework. Contains .feature files with 
scenarios and steps that are used in those scenarios.

`page_objects`: contain the page object models to interact with the website via 
a friendly API.

So to summarize, a feature file present in `features` folder, contains one or 
more scenarios that are a suite of steps. Those steps act like a glue layer 
to do some actions on a page with real data from `data`. The actions on a page 
are done via a class that is a representation of this page and is present in 
the `page_obects` folder. A page is composed of 0 or n components present 
in `components` folder.