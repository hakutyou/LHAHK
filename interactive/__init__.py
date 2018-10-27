# coding=utf-8

__all__ = ['qmlReceiver', 'qmlCaller']

from . import qmlReceive
from . import qmlCall


qmlReceiver = qmlReceive.QmlReceive()   # 被调用
qmlCaller = qmlCall.QmlCall()           # 调用
