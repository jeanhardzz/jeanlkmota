mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"jeanlk@dcc.ufmg.br\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
base=\"light\"\n\
primaryColor=\"purple\"\n\
\n\
" > ~/.streamlit/config.toml