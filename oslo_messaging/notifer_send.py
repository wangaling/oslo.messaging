#notifier_send.py
from oslo.config import cfg
import oslo_messaging

transport = oslo_messaging.get_transport(cfg.CONF)
notifier = messaging.Notifier(transport,driver='messaging',topic='notifications')
notifier2 = notifier.prepare(publisher_id='compute')
notifier2.error(ctxt={},event_type='my_type',payload = {'content':'error occurred'})





