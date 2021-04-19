# playbook

ansible playbook for daily ops

# example

目前机器加用户和权限管理全部由 @wangpengcheng 管理

ansible 有时候会有兼容性问题，目前使用的是 python3.8 环境下的 ansible-playbook 2.9.11

机器列表维护在 host.py 里，示例使用方式
```bash
ansible-playbook -i host.py add-users-senses.yaml
```
