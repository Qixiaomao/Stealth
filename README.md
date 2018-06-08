# Description
这是一款收集CMS、WHOIS、DNS、robots.txt、子域名、端口信息，系统信息、服务信息的工具
# Operating  environment
> 
>python 3+
>  
>linux or windows
>
>nmap

# Installation guide 
> linux 
> 
> git clone https://github.com/Qixiaomao/Stealth.git
>
>pip install -r requirements.txt
>
>
>


# Strcuture

```
.
├── config（配置文件）
│   ├── cms.txt
│   └── config.py

├── README.md（说明文档）
├── requirements.txt（依赖库）
├── static（静态资源目录）
│   ├── Bootsrap.css
│   ├── main.css
│   ├── subdomian.css
│   ├── whois_base.css
│   └── whois.css
├── Stealth.py(主函数)
└── util（功能函数目录）
    ├── cms_info.py
    ├── dns_info.py
    ├── help.py
    ├── http_request.py
    ├── is_select.py
    ├── nmap_port_info.py
    ├── output_html.py
    ├── robots.py
    ├── subdomain.py
    ├── termcolor.py
    ├── termcolor.pyc
    ├── welcome.py
    └── who_is.py


