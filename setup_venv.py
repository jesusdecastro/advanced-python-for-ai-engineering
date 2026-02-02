#!/usr/bin/env python3
"""
Script to set up virtual environment with venv and install dependencies.
"""
import os
import sys
import subprocess
import platform

def main():
    print("🐍 Setting up virtual environment for Advanced Python for AI course\n")
    
    # Detect operating system
    system = platform.system()
    print(f"Operating system detected: {system}")
    
    # Create virtual environment
    print("\n📦 Creating virtual environment...")
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ Virtual environment created successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating virtual environment: {e}")
        return 1
    
    # Determine pip executable path
    if system == "Windows":
        pip_path = os.path.join("venv", "Scripts", "pip.exe")
        activate_cmd = r"venv\Scripts\activate"
    else:
        pip_path = os.path.join("venv", "bin", "pip")
        activate_cmd = "source venv/bin/activate"
    
    # Update pip
    print("\n🔄 Updating pip...")
    try:
        subprocess.run([pip_path, "install", "--upgrade", "pip"], check=True)
        print("✅ pip updated")
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Warning updating pip: {e}")
    
    # Install dependencies
    if os.path.exists("requirements.txt"):
        print("\n📚 Installing dependencies from requirements.txt...")
        try:
            subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
            print("✅ Dependencies installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error installing dependencies: {e}")
            return 1
    else:
        print("\n⚠️  requirements.txt not found")
    
    print("\n" + "="*60)
    print("✨ Environment configured successfully!")
    print("="*60)
    print(f"\nTo activate the virtual environment, run:")
    print(f"  {activate_cmd}")
    print("\nTo start Jupyter Notebook:")
    print("  jupyter notebook")
    print("\nHappy learning! 🚀")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
