import subprocess
import sys

def install_dependencies():
    print("Installing dependencies...")
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)

def run_tests():
    print("Running tests...")
    subprocess.run([sys.executable, '-m', 'pytest', 'tests'], check=True)

def package_application():
    print("Packaging application...")
    # Add packaging steps if needed

if _name_ == "_main_":
    try:
        install_dependencies()
        run_tests()
        package_application()
        print("Build succeeded!")
    except subprocess.CalledProcessError as e:
        print(f"Build failed with error: {e}")
        sys.exit(1)
