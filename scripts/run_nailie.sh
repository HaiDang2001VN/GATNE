rm -rf ./GATNE/data/nailie/model
python ./GATNE/src/main.py --input ./GATNE/data/nailie \
        --epoch 20 --batch-size 1024 --eval-type booking \
        --att-dim 64 --dimensions 256 --edge-dim 32 \
        --num-walks 4 --model_path ./GATNE/data/nailie/model \
        --patience 3 --schema client-post-client,client-menu-client,post-nailist-post,menu-nailist-menu