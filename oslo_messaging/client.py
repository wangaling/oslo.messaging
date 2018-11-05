#client.py

from oslo.config import cfg
import oslo_messaging
transport = oslo_messaging.get_transport(cfg.CONF)
target = oslo_messaging.Target(topic='test')
client = oslo_messaging.RPCClient(transport,target)
ret = client.call(ctxt = {}, method = 'test',arg = 'myarg')
cctxt = client.prepare(namespace='control',version='2.0')
cctxt.cast({},'stop')


