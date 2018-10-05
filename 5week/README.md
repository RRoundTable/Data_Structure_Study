### 구성요소


#### check list
- 왜 line별로 Queue와 Stack를 따로 썻는가? 선입선출법과 후입선출법을 비교하기 위해서

- matCost와 matShortestCost의 관계는? matCost는 processes[row][col].getSize()로 구하며, matShortestCost는 matcost에 이전 matShortestCost의 영향을 받는다.

- cross over가 안된다 : 라인이 독립적으로 운영된다.


#### class
	• Factory.py 
		○ Variable : breakProb, waitingProduct, completeProduct
		○ selectLine() : 2개의 라인 중에서 더 빠른 라인을 선택한다.
		○ getCostMatrix() : 소요되는 시간 matrix를 구하여준다.
		○ Run() : 
	• main.py
		○ Variable :  filename, error
		○ 프로그램을 실행한다. 파일명과 에러확률을 입력한다.
		
	• ManufacturingProcess.py
		○ Variable :  waitingLine(Queue or Stack)
		○ arriveProduct(plan) : plan을 추가한다. / plan : 
		○ leaveProduct() :  plan을 반환한다.
		○ getSize() : 다음 node의 size
		○ getListString() : 
		
	• PlanNode.py : double linked list
		○ Variable : numNo, strSerialNumber, numModelNumber, dateStart, numAssemblyOrder, dateEnd, strOrderOrigin, prevNode, nextNode
		○ PrintOut() : node의 정보를 출력한다.
		○ getNextNode() : 다음 노드 반환
		○ getPrevNode() : 이전 노드 반환
		○ setNextNode() : 다음 노드 설정
		○ setPrevNode() : 이전 노드 설정
		
	• ProductionList.py : double linked list 확장버전
		○ Variable : nodeHead, nodeTail
		○ showPlanChart() :
		○ addLast() : 마지막 노드로 추가한다
		○ addFirst() : 첫번째 노드로 추가한다
		○ removeLast() :  마지막 노드를 제거한다.
		○ removeFirst() : 첫 번째 노드를 제거한다.
		○ getSize() : 해당 노드의 남은 노드의 사이즈를 반환한다.
		○ getListString() : node의 numNo을 반환한다.
		
	• Queue.py
		○ Variable : List
		○ Queue : LIFO
		○ add(self, object) : addLast(object) 마지막에 노드 추가하기
		○ get() : removeFirst()로 제거하기, 첫번째 노드 반환
		○ getSize() : 다음 노드의 size 구하기
		○ getListString()
		
	• Stack.py
		○ Variable : List
		○ Stack : FIFO
		○ add(self, object) : addFirst()로 노드추가하기
		○ get() : removeFirst()로 제거하기, 첫번째 노드 반환(제거하는 노드)
		○ getSize() : 다음 노드의 size
		○ getListString()
		
	• Plan-2012.12.24.csv : data file


