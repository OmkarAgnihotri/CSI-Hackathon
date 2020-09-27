from compute import Classifier
text = 'Deadlock is state where a process is waiting for a resource which is held by another process which in turn is waiting for a resource which is held by the first process. It is state of circular wait'
answer = 'In an operating system, a deadlock occurs when a process or thread enters a waiting state because a requested system resource is held by another waiting process, which in turn is waiting for another resource held by another waiting process.'

classifier = Classifier()

classifier.fit(text,answer)

classifier.predict()