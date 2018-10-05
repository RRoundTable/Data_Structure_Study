### 구성요소


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


