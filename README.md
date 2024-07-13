<h1 align="center" id="title">Automated Discounted Cash Flow</h1>

<p id="description">
    This tool is designed to calculate the perceived value of a company based strictly on quantitative figures. 
</p>

<h2>Key Features</h2>
<ul>
    <li><b>Quantitative Analysis:</b> Utilizes hard data from analyst estimates and market indicators.</li>
    <li><b>DCF Calculation:</b> Automates the DCF process, providing a streamlined method to estimate the intrinsic value of companies. Measures indictators to determine whether to utilize a 5 or 10 forecast</li>
    <li><b>Customizable Inputs:</b> Allows users to input their own assumptions for various parameters to see how they affect the valuation.</li>
    <li><b>Comprehensive Output:</b> Generates detailed reports on the estimated intrinsic value, including all intermediate calculations.</li>
</ul>



<h2>Key Features</h2>
<ul>
    <li><b>Quantitative Analysis:</b>
        <ul>
            <li>Utilizes hard data from analyst estimates for EBIT and revenue growth.</li>
            <li>Incorporates current perpetual growth rates like 2-year government bond rates.</li>
        </ul>
    </li>
    <li><b>Automated DCF Calculation:</b>
        <ul>
            <li>Automates the Discounted Cash Flow (DCF) process to estimate the intrinsic value of companies.</li>
            <li>Evaluates multiple factors to determine whether to utilize a 5-year or 10-year DCF analysis, including revenue growth variability, stock lifetime, and sector stability.</li>
        </ul>
    </li>
    <li><b>Customizable Inputs:</b>
        <ul>
            <li>Allows users to input their own assumptions for various parameters such as reinvestment rates, tax rates, and growth rates to see how these affect the valuation.</li>
        </ul>
    </li>
    <li><b>Comprehensive Data Integration:</b>
        <ul>
            <li>Fetches detailed financial statements (balance sheets, income statements, and cash flow statements) from Financial Modeling Prep API.</li>
            <li>Calculates industry-specific metrics like unlevered beta and industry reinvestment rates using data from company peers.</li>
            <li>Integrates country-specific equity risk premiums and macroeconomic indicators from sources like FRED API and Yahoo Finance.</li>
        </ul>
    </li>
    <li><b>Advanced Financial Metrics:</b>
        <ul>
            <li>Computes Weighted Average Cost of Capital (WACC) considering market risk premiums, cost of debt, and cost of equity.</li>
            <li>Estimates terminal value using final year free cash flow to firm (FCFF) and perpetual growth rate.</li>
            <li>Calculates historical and industry reinvestment rates, adjusting for capital expenditure and working capital changes.</li>
        </ul>
    </li>
    <li><b>Error Handling and Debugging:</b>
        <ul>
            <li>Implements try-except blocks to manage API request errors and ensure continuous data retrieval.</li>
            <li>Provides detailed print statements for debugging and monitoring the data fetching process.</li>
        </ul>
    </li>
    <li><b>Detailed Output Reports:</b>
        <ul>
            <li>Generates detailed reports on all intermediate calculations including reinvestment rates, WACC components, and FCFF.</li>
            <li>Offers a final fair value estimation compared against current market value, including a sensitivity analysis to see different trends.</li>
        </ul>
    </li>
    <li><b>Technical Analysis Integration:</b>
        <ul>
            <li>Adjusts levered beta for tax and debt-equity ratios to derive unlevered beta for industry comparison.</li>
            <li>Analyzes revenue growth variability to assess stability and predictability of future cash flows.</li>
        </ul>
    </li>
    <li><b>Historical Data Utilization:</b>
        <ul>
            <li>Leverages historical financial data to calculate trimmed mean reinvestment rates and historical revenue growth patterns.</li>
            <li>Utilizes long-term historical data to support more accurate future projections in the DCF model.</li>
        </ul>
    </li>
    <li><b>Comprehensive Assumptions and Outputs:</b>
        <ul>
            <li>Clearly documents assumptions for EBIT margins, revenue growth, tax rates, and FCFF.</li>
            <li>Considers non-current assets, net liabilities, and cash holdings in the final equity value calculation.</li>
        </ul>
    </li>
</ul>

<h2>Why DCF is Subjective</h2>
<p>
    While DCF is a powerful tool for valuation, it's important to understand its inherent subjectivity due to several factors:
</p>

<h3>Qualitative Factors</h3>
<ul>
    <li><b>Market Sentiment:</b> Investor psychology and market conditions can lead to deviations from intrinsic value.</li>
    <li><b>Competitive Landscape:</b> Industry dynamics, competitive positioning, and potential market disruptions are qualitative factors that aren't fully captured by quantitative models.</li>
    <li><b>Management Quality:</b> The effectiveness of a company's leadership and their strategic decisions can influence future performance.</li>
</ul>

<h3>Changing Fundamentals</h3>
<ul>
    <li><b>Economic Conditions:</b> Macroeconomic factors and geopolitical events can alter a company's future prospects.</li>
    <li><b>Technological Advancements:</b> Innovation and technological changes can impact a company’s growth trajectory and competitive advantage.</li>
</ul>

<h2>Project Scope</h2>
<p>
    This project focuses on the quantitative aspects of DCF analysis, providing a robust framework to calculate perceived value based on the following inputs:
</p>
<ul>
    <li><b>Analyst EBIT Estimates:</b> Earnings before interest and taxes as projected by financial analysts.</li>
    <li><b>Analyst Revenue Growth Estimates:</b> Expected growth rates for company revenue.</li>
    <li><b>Perpetual Growth Rate:</b> Typically derived from long-term government bond yields to represent a stable growth rate.</li>
    <li><b>Effective Tax Rate Predictions:</b> Anticipated tax rates applied to future earnings.</li>
</ul>

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone the Repository:</p>

```
git clone https://github.com/realjake/Automated-DCF.git
```

<p>Navigate into the cloned repo</p>

```
cd AutomatedDCF
```


<p>2. Install Required Dependencies:</p>

```
pip install -r requirements.txt
```


<p>3. Edit .env file and add your Financial Modeling Prep API key:</p>

```
--> AutomatedDCF / .env / FMP_API_KEY=XXXXXXXX
```

<h2>Contributing</h2>
<p>
    We welcome contributions both financial and technical insight to enhance the functionality and accuracy of this tool. Please submit pull requests or open issues for any bugs or feature requests. Feel free to contact me on [Linkedin](https://www.linkedin.com/in/jakeclowers/))
</p>

<h2>License</h2>
<p>
    This project is licensed under the MIT License. See the LICENSE file for details.
</p>

<h2>Acknowledgements</h2>
<p>
    Special thanks to all the contributors and the financial analyst community for providing the necessary data and insights to build this tool. 
</p>
