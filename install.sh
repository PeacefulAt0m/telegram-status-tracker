if [[ ! -d "env/bin" ]]; then
    sudo apt -y install python3
    sudo apt -y install python3-pip
    python3 -m pip install --user virtualenv
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    echo "Installation completed"
else
    echo "Requirements already satisfied"
fi
