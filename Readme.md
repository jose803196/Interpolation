<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; line-height: 1.6; color: #333;">
    <header style="text-align: center; border-bottom: 2px solid #007BFF; padding-bottom: 10px;">
        <h1 style="color: #007BFF; font-size: 2.5em;">Interpolations</h1>
        <p style="font-size: 1.2em; color: #555;">A Python-based interpolation library for fitting data using various regression models.</p>
    </header>
    <section style="margin-top: 20px;">
        <h2 style="color: #005566; font-size: 1.8em; border-left: 4px solid #007BFF; padding-left: 10px;">Overview</h2>
        <p>
            <strong>Interpolations</strong> is a Python application designed to perform data interpolation using different regression models. 
            It allows users to input data points and fit them to linear, exponential, quadratic, cubic, power, hyperbolic, or logarithmic models.
            Each model calculates the best-fit parameters and provides an error estimate.
        </p>
    </section>
    <section style="margin-top: 20px;">
        <h2 style="color: #005566; font-size: 1.8em; border-left: 4px solid #007BFF; padding-left: 10px;">Supported Models</h2>
        <p>The library includes the following regression models, each implemented as a class:</p>
        <ol style="padding-left: 20px;">
            <li style="margin-bottom: 10px;">
                <strong>Linear:</strong> <code>y = mx + b</code>
                <p style="margin: 5px 0 0 20px; color: #555;">Fits a straight line to the data.</p>
            </li>
            <li style="margin-bottom: 10px;">
                <strong>Exponential:</strong> <code>y = e<sup>mx + b</sup></code>
                <p style="margin: 5px 0 0 20px; color: #555;">Fits an exponential curve using logarithmic transformation.</p>
            </li>
            <li style="margin-bottom: 10px;">
                <strong>Quadratic:</strong> <code>y = ax<sup>2</sup> + bx + c</code>
                <p style="margin: 5px 0 0 20px; color: #555;">Fits a second-degree polynomial to the data.</p>
            </li>
            <li style="margin-bottom: 10px;">
                <strong>Cubic:</strong> <code>y = ax<sup>3</sup> + bx<sup>2</sup> + cx + d</code>
                <p style="margin: 5px 0 0 20px; color: #555;">Fits a third-degree polynomial to the data.</p>
            </li>
            <li style="margin-bottom: 10px;">
                <strong>Power:</strong> <code>y = ax<sup>b</sup></code>
                <p style="margin: 5px 0 0 20px; color: #555;">Fits a power-law model using logarithmic transformation.</p>
            </li>
            <li style="margin-bottom: 10px;">
                <strong>Hyperbolic:</strong> <code>y = a + b/x</code>
                <p style="margin: 5px 0 0 20px; color: #555;">Fits a hyperbolic curve to the data.</p>
            </li>
            <li style="margin-bottom: 10px;">
                <strong>Logarithmic:</strong> <code>y = a + b ln(x)</code>
                <p style="margin: 5px 0 0 20px; color: #555;">Fits a logarithmic model to the data.</p>
            </li>
        </ol>
    </section>
    <section style="margin-top: 20px;">
        <h2 style="color: #005566; font-size: 1.8em; border-left: 4px solid #007BFF; padding-left: 10px;">Installation</h2>
        <p>To use the Interpolations library, follow these steps:</p>
        <ol style="padding-left: 20px;">
            <li>Ensure you have Python 3.6+ installed.</li>
            <li>Install the required dependencies: <code>numpy</code> and <code>matplotlib</code> (optional, for plotting).</li>
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px;">
pip install numpy matplotlib
            </pre>
            <li>Clone or download the repository and navigate to the project directory.</li>
            <li>Run the main script: <code>python main.py</code>.</li>
        </ol>
    </section>
    <section style="margin-top: 20px;">
        <h2 style="color: #005566; font-size: 1.8em; border-left: 4px solid #007BFF; padding-left: 10px;">Usage</h2>
        <p>
            Run <code>main.py</code> to start the application. You will be prompted to:
        </p>
        <ul style="padding-left: 20px;">
            <li>Enter the number of data points.</li>
            <li>Input the <code>x</code> and <code>y</code> values for each point.</li>
            <li>Select a regression model (work in progress).</li>
        </ul>
        <p>
            The program will output the model parameters and an error estimate. Optionally, it can generate a plot of the data and fitted curve (if <code>matplotlib</code> is installed).
        </p>
    </section>
    <section style="margin-top: 20px;">
        <h2 style="color: #005566; font-size: 1.8em; border-left: 4px solid #007BFF; padding-left: 10px;">Requirements</h2>
        <ul style="padding-left: 20px;">
            <li><strong>Python:</strong> Version 3.6 or higher.</li>
            <li><strong>Dependencies:</strong> <code>numpy</code> (required), <code>matplotlib</code> (optional for visualization).</li>
        </ul>
    </section>
    <section style="margin-top: 20px;">
        <h2 style="color: #005566; font-size: 1.8em; border-left: 4px solid #007BFF; padding-left: 10px;">Contributing</h2>
        <p>
            Contributions are welcome! Feel free to submit issues or pull requests to improve the library, add new features, or enhance documentation.
        </p>
    </section>
    <footer style="margin-top: 30px; text-align: center; border-top: 1px solid #ddd; padding-top: 10px; color: #555;">
        <p>Developed by Jose Lopez. Licensed under MIT License.</p>
    </footer>
</body>
</html>