rm -rf ./GATNE/data/nailie/model
python ./GATNE/src/run.py --input ./GATNE/data/nailie \
        --epoch 20 --batch-size 1024 --eval-type booking \
        --att-dim 64 --dimensions 256 --edge-dim 32 \
        --num-walks 6 --model_path ./GATNE/data/nailie/model \
        --patience 3 --schema client-menu-client,menu-nailist-menu,nailist-client-nailist