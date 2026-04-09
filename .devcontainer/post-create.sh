echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
echo 'export LANG=C.UTF-8' >> "$HOME/.bashrc"
echo 'export LC_ALL=C.UTF-8' >> "$HOME/.bashrc"

# Clone epiworld source for API documentation generation
if [ ! -d "epiworld-src" ]; then
    git clone --depth 1 https://github.com/UofUEpiBio/epiworld.git epiworld-src
fi