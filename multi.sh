if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/KR-Botz/KR-MULTI-BOT.git /KR-MULTI-BOT     
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /KR-MULTI-BOT
fi
cd /KR-MULTI-BOT
pip3 install -U -r requirements.txt
echo "Bot is start✨ By @Kr_Botz"
python3 loader.py
