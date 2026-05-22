import importlib


PACKAGES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready"
}


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    here = {}
    miss = []

    for name, description in PACKAGES.items():
        try:
            module = importlib.import_module(name)

            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {name} ({version}) - {description}")
            here[name] = module
        except ImportError:
            print(f"[MISSING] {name} - not installed")
            miss.append(name)

    if miss:
        print("\nInstall with:")
        print("pip install -r requirements.txt")
        print("or")
        print("poetry install")
    else:
        numpy = here["numpy"]
        pandas = here["pandas"]
        plot = importlib.import_module("matplotlib.pyplot")

        print("\nAnalyzing Matrix data...")
        print("Processing 1000 data points...")
        print("Generating visualization...")
        data = numpy.random.randn(1000)
        df = pandas.DataFrame(data, columns=["values"])

        plot.scatter(range(len(df)), df["values"])
        plot.savefig("matrix_analysis.png")
        plot.close()

        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")
