---
layout: jumbotron
jumbo_title: Community Data Analysis Tools
jumbo subtitle:
jumbo_text: CDAT is a powerful and complete front-end to a rich set of visual-data exploration and analysis capabilities well suited for data analysis problems.
---

<div class="container">
  <div class="alert alert-warning">
    <p>
      <strong>Warning</strong> The CDAT library is now in maintenance-only mode, with plans for deprecation and cease of support around the end of calendar year 2023. Until this time, the dependencies for specific CDAT packages (`cdms2`, `cdat_info`, `cdutil`, `cdtime`, `genutil`, `libcdms`) will be monitored to ensure they build and install in Conda environments. We currently support Python versions 3.7, 3.8, 3.9, and 3.10. Unfortunately, feature requests and bug fixes will no longer be addressed.
    </p>
  </div>
<div class="alert alert-success">
    <p>
      If you are interested in an alternative solution, please check out the <a href="https://github.com/pydata/xarray">xarray</a> and <a href="https://github.com/xCDAT/xcdat">xCDAT - Xarray Extended With Climate Data Analysis Tools</a> projects.
    </p>
</div>

<h2 id="new">Welcome to CDAT!</h2>

New here? Don't worry! We'll help you get started. If you're interested in what you can do with CDAT, you can take a look at our [gallery]. If you're interested in anything you see there, you can look into getting our application [installed][install]. Once CDAT has been installed, check out our [Getting Started][getting_started] guide.

<h2 id="help">We'll give you a hand.</h2>

Having trouble with something? We've got a great community of people who can give you a hand on our [support] email list.

<h2 id="contribute">We're on GitHub!</h2>

If you want to get to know us, you can come chat with us on our [developer mail list][dev]. If you want to get up to speed with the project, our [wiki] is kept up-to-date with what you need to get going.

<h2 id="info">The CDAT Project</h2>
<p>
CDAT builds on the following key technologies:
<ol>
  <li>Python and its ecosystem (e.g. NumPy, Matplotlib);</li>
  <li>Jupyter Notebooks and iPython;</li>
  <li>A toolset developed at LLNL for the analysis, visualization, and management of large-scale distributed climate data;</li>
  <li>VTK, the Visualization Toolkit, which is open source software for manipulating and displaying scientific data.</li>
</ol>
</p>
<p>

These combined tools, along with others such as the R open-source statistical
analysis and plotting software and custom packages (e.g. DV3D), form CDAT
and provide a synergistic approach to climate modeling, allowing researchers to
advance scientific visualization of large-scale climate data sets. The CDAT
framework couples powerful software infrastructures through two primary means:

<ol>
  <li>Tightly coupled integration of the CDAT Core with the VTK infrastructure to provide high-performance, parallel-streaming data analysis and visualization of massive climate-data sets (other tighly coupled tools include
  VCS, DV3D, and ESMF/ESMP);</li>
  <li>Loosely coupled integration to provide the flexibility of using tools quickly
  in the infrastructure such as ViSUS or R for data analysis and
  visualization as well as to apply customized data analysis applications within
  an integrated environment.</li>
</ol>
</p>
<p>
Within both paradigms, CDAT will provide data-provenance capture and
mechanisms to support data analysis.
</p>

CDAT is licensed under the [BSD-3][bsd3] license.

<h3>U.S. Sponsors</h3>
<div class="sponsor_image">
  <img src="/images/doe.svg" class="thumbnail" />
</div>
<div class="sponsor_image">
  <img src="/images/nasa.svg" class="thumbnail" />
</div>

[gallery]: /gallery.html
[install]: https://github.com/CDAT/cdat/wiki/install
[getting_started]: /getting_started.html
[support]: mailto:CDAT-SUPPORT@LISTSERV.LLNL.GOV?body=subscribe%20cdat-support
[dev]: mailto:CDAT-DEV@LISTSERV.LLNL.GOV?body=subscribe%20cdat-dev
[wiki]: https://github.com/CDAT/cdat/wiki
[bsd3]: https://opensource.org/licenses/BSD-3-Clause

<!-- &amp;subject=Subscribe -->
