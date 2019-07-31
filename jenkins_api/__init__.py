# -*- coding: utf-8 -*-
# @Time    : 2019-07-26 20:23
# @Author  : Eylaine
# @File    : __init__.py

from jenkins import Jenkins

from settings import JENKINS_URL as URL
from settings import JENKINS_PASSWORD as PASSWORD
from settings import JENKINS_USERNAME as USERNAME
from settings import JENKINS_JOB_NAME as JOB_NAME


"""python-jenkins模块的使用和常用方法"""
jenkins = Jenkins(URL, USERNAME, PASSWORD)

# 获取所有的jobs
all_jobs = jenkins.get_all_jobs()

# 根据job name获取info，返回json
job_info = jenkins.get_job_info(JOB_NAME)

# 最后一次build的信息，包含num和url
last_build = job_info["lastBuild"]
# 最后一次build的number，int类型
NUMBER = last_build["number"]

build_info = jenkins.get_build_info(JOB_NAME, NUMBER)
info = jenkins.get_info()

# 运行日志
console_text = jenkins.get_build_console_output(JOB_NAME, NUMBER)
