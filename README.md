<div id="top" class="">

<div align="center" class="text-center">
<h1>WATER-MONITOR</h1>
<p><em>Transforming Water Data into Actionable Insights</em></p>

<img alt="last-commit" src="https://img.shields.io/github/last-commit/21PachaGod/Water-monitor?style=flat&amp;logo=git&amp;logoColor=white&amp;color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
<img alt="repo-top-language" src="https://img.shields.io/github/languages/top/21PachaGod/Water-monitor?style=flat&amp;color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
<img alt="repo-language-count" src="https://img.shields.io/github/languages/count/21PachaGod/Water-monitor?style=flat&amp;color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
<p><em>Built with the tools and technologies:</em></p>
<img alt="Markdown" src="https://img.shields.io/badge/Markdown-000000.svg?style=flat&amp;logo=Markdown&amp;logoColor=white" class="inline-block mx-1" style="margin: 0px 2px;">
<img alt="Python" src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&amp;logo=Python&amp;logoColor=white" class="inline-block mx-1" style="margin: 0px 2px;">
</div>
<br>
<hr>
<h2>Table of Contents</h2>
<ul class="list-disc pl-4 my-0">
<li class="my-0"><a href="#overview">Overview</a></li>
<li class="my-0"><a href="#getting-started">Getting Started</a>
<ul class="list-disc pl-4 my-0">
<li class="my-0"><a href="#prerequisites">Prerequisites</a></li>
<li class="my-0"><a href="#installation">Installation</a></li>
<li class="my-0"><a href="#usage">Usage</a></li>
<li class="my-0"><a href="#testing">Testing</a></li>
</ul>
</li>
</ul>
<hr>
<h2>Overview</h2>
<p>Water-monitor is an embedded system designed to measure and analyze water temperatures at multiple depths, leveraging Arduino Nano 33 BLE Sense Rev 2. It combines environmental sensing with GPS data logging to provide comprehensive spatial and temporal insights.</p>
<p><strong>Why Water-monitor?</strong></p>
<p>This project enables precise environmental data collection and validation in outdoor or remote settings. The core features include:</p>
<ul class="list-disc pl-4 my-0">
<li class="my-0">🛰️ <strong>GPS Integration:</strong> Log geospatial data to contextualize temperature readings.</li>
<li class="my-0">📊 <strong>Data Storage:</strong> Save measurements reliably on SD cards for later analysis.</li>
<li class="my-0">🌡️ <strong>Multi-Depth Sensing:</strong> Capture temperature variations at different water depths.</li>
<li class="my-0">🖥️ <strong>Real-Time Visualization:</strong> Display key data on OLED screens for immediate insights.</li>
<li class="my-0">🔍 <strong>Data Processing:</strong> Extract and analyze stored sensor data for trend detection.</li>
<li class="my-0">🚀 <strong>Modular Architecture:</strong> Designed for flexible deployment in environmental monitoring systems.</li>
</ul>
<hr>
<h2>Getting Started</h2>
<h3>Prerequisites</h3>
<p>This project requires the following dependencies:</p>
<ul class="list-disc pl-4 my-0">
<li class="my-0"><strong>Programming Language:</strong> Python</li>
<li class="my-0"><strong>Package Manager:</strong> Conda</li>
</ul>
<h3>Installation</h3>
<p>Build Water-monitor from the source and install dependencies:</p>
<ol>
<li class="my-0">
<p><strong>Clone the repository:</strong></p>
<pre><code class="language-sh">❯ git clone https://github.com/21PachaGod/Water-monitor
</code></pre>
</li>
<li class="my-0">
<p><strong>Navigate to the project directory:</strong></p>
<pre><code class="language-sh">❯ cd Water-monitor
</code></pre>
</li>
<li class="my-0">
<p><strong>Install the dependencies:</strong></p>
</li>
</ol>
<p><strong>Using <a href="https://docs.conda.io/">conda</a>:</strong></p>
<pre><code class="language-sh">❯ conda env create -f conda.yml
</code></pre>
<h3>Usage</h3>
<p>Run the project with:</p>
<p><strong>Using <a href="https://docs.conda.io/">conda</a>:</strong></p>
<pre><code class="language-sh">conda activate {venv}
python {entrypoint}
</code></pre>
<h3>Testing</h3>
<p>Water-monitor uses the {<strong>test_framework</strong>} test framework. Run the test suite with:</p>
<p><strong>Using <a href="https://docs.conda.io/">conda</a>:</strong></p>
<pre><code class="language-sh">conda activate {venv}
pytest
</code></pre>
<hr>
<div align="left" class=""><a href="#top">⬆ Return</a></div>
<hr></div>
