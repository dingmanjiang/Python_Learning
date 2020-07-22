
## 创建
	python3 -m venv myvenv

## 创建使用系统配置
	python3 -m venv myvenv --system-site-packages

## 进入shell
source myvenv/bin/activate

## 输出安装配置
	pip freeze > requirements.txt

## 输入安装配置
	pip install -r requirements.txt

## 现实本环境安装的配置
	pip list --local

## 退出shell
	deactivate

## 删除myvenv
	rm -rf myvenv/