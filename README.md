# PythonProgramFiles

我的所有 Python 项目

## 目录及简介

> 太懒了，过后补全

- [RFM](RFM) &#x2002; 之前为学习 RFM 数据分析方法而写的代码
- [其他](其他)  &#x2002; 纯杂物
- [算法](算法) &#x2002; 为学习算法而写，大部分跟 [`acwing`](https://www.acwing.com/)
    - [算法基础](算法/Basic) &#x2002;
      内容全部来自[`算法基础课`](https://www.acwing.com/activity/content/11/)
        - [基础算法](算法/Basic/BasicAlgorithms) &#x2002; 包括排序、二分、高精度、前缀和与差分、双指针算法、位运算、离散化、区间合并等内容。
        - [数据结构](算法/Basic/DataStructure) &#x2002; 包括单链表，双链表，栈，队列，单调栈，单调队列，KMP，Trie，并查集，堆，哈希表等内容。
        - [搜索与图论](算法/Basic/SearchAndGraphTheory) &#x2002;
          包括DFS，BFS，树与图的深度优先遍历，树与图的广度优先遍历，拓扑排序，Dijkstra，bellman-ford，spfa，Floyd，Prim，Kruskal，染色法判定二分图，匈牙利算法等内容。
        - [数学知识](算法/Basic/MathematicalKnowledge) &#x2002;
          包括质数，约数，欧拉函数，快速幂，扩展欧几里得算法，中国剩余定理，高斯消元，求组合数，容斥原理，博弈论等内容。
        - [动态规划](算法/Basic/DynamicProgramming) &#x2002;
          包括背包问题，线性DP，区间DP，计数类DP，数位统计DP，状态压缩DP，树形DP，记忆化搜索等内容。
            - [`数位统计DP`](https://www.acwing.com/activity/content/problem/content/1009/) &#x2002; 写起来太麻烦，没写
            - [状态压缩DP](算法/Basic/DynamicProgramming/StateCompressedDP)
                - [蒙德里安的梦想](算法/Basic/DynamicProgramming/StateCompressedDP/MondrianDream.py)
                - [最短Hamilton路径](算法/Basic/DynamicProgramming/StateCompressedDP/ShortestHamiltonPath.py)
            - [树形DP](算法/Basic/DynamicProgramming/TreeDP.py)
            - [记忆化搜索](算法/Basic/DynamicProgramming/MemorySearch.py)
        - [贪心](算法/Basic/Greed) &#x2002; 包括区间问题，Huffman树，排序不等式，绝对值不等式，推公式等内容。
            - [区间问题](算法/Basic/Greed/IntervalProblem)
                - [区间选点、最大不相交区间数量](算法/Basic/Greed/IntervalProblem/IntervalSelection.py)
                - [区间分组](算法/Basic/Greed/IntervalProblem/IntervalGrouping.py)
                - [区间覆盖](算法/Basic/Greed/IntervalProblem/IntervalCoverage.py)
            - [Huffman 树](算法/Basic/Greed/HuffmanTree.py)
            - [排序不等式](算法/Basic/Greed/OrderingInequality.py)
            - [绝对值不等式](算法/Basic/Greed/AbsoluteValueInequality.py)
            - [推公式](算法/Basic/Greed/PushFormula.py)
    - [算法提高课](算法/Improve) &#x2002; 内容全部来自[`算法提高课`](https://www.acwing.com/activity/content/16/)
        - [动态规划](算法/Improve/DynamicProgramming) &#x2002;
          包括数字三角形模型、最长上升子序列模型、背包模型、状态机、状态压缩DP、区间DP、树形DP、数位DP、单调队列优化DP、斜率优化DP等内容
            - [数字三角形模型](算法/Improve/DynamicProgramming/DigitalTriangleModel)
                - [摘花生](算法/Improve/DynamicProgramming/DigitalTriangleModel/PickingPeanuts.py)
                - [最低通行费](算法/Improve/DynamicProgramming/DigitalTriangleModel/MinimumToll.py)
                - [方格取数](算法/Improve/DynamicProgramming/DigitalTriangleModel/SquareAccess.py)
                - [传纸条](算法/Improve/DynamicProgramming/DigitalTriangleModel/PassNote.py)
            - [最长上升子序列模型](算法/Improve/DynamicProgramming/LongestAscendingSubsequence)
                - [怪盗基德的滑翔翼](算法/Improve/DynamicProgramming/LongestAscendingSubsequence/HangGliding.py)
                - [登山](算法/Improve/DynamicProgramming/LongestAscendingSubsequence/Mountaineering.py)
                - [合唱队形](算法/Improve/DynamicProgramming/LongestAscendingSubsequence/ChorusFormation.py)
                - [友好城市](算法/Improve/DynamicProgramming/LongestAscendingSubsequence/SisterCity.py)
                - [最大上升子序列和](算法/Improve/DynamicProgramming/LongestAscendingSubsequence/ToSum.py)
                - [拦截导弹](算法/Improve/DynamicProgramming/LongestAscendingSubsequence/InterceptorMissile.py)
                - [导弹防御系统](算法/Improve/DynamicProgramming/LongestAscendingSubsequence/Mountaineering.py)
                - [最长公共上升子序列](算法/Improve/DynamicProgramming/LongestAscendingSubsequence/Common.py)
            - [背包模型](算法/Improve/DynamicProgramming/BackpackModel)
                - [采药](算法/Improve/DynamicProgramming/BackpackModel/CollectHerbs.py)
                - [装箱问题](算法/Improve/DynamicProgramming/BackpackModel/PackingProblem.py)
                - [宠物小精灵之收服](算法/Improve/DynamicProgramming/BackpackModel/PokemonConquer.py)
                - [数字组合](算法/Improve/DynamicProgramming/BackpackModel/NumberCombinations.py)
                - [买书](算法/Improve/DynamicProgramming/BackpackModel/BuyBooks.py)
                - [货币系统](算法/Improve/DynamicProgramming/BackpackModel/MonetarySystem.py)
                - [货币系统-NOIP](算法/Improve/DynamicProgramming/BackpackModel/MonetarySystemNOIP.py)
                - [多重背包问题 III](算法/Improve/DynamicProgramming/BackpackModel/MultipleKnapsackIII.py)
                - [庆功会](算法/Improve/DynamicProgramming/BackpackModel/VictoryMeeting.py)
                - [混合背包问题](算法/Improve/DynamicProgramming/BackpackModel/MixedKnapsack.py)
                - [二维费用的背包问题](算法/Improve/DynamicProgramming/BackpackModel/TwoDimensionalCost.py)
                - [潜水员](算法/Improve/DynamicProgramming/BackpackModel/Diver.py)
                - [机器分配](算法/Improve/DynamicProgramming/BackpackModel/MachineDistribution.py)
                - [开心的金明](算法/Improve/DynamicProgramming/BackpackModel/HappyJinMing.py)
                - [有依赖的背包问题](算法/Improve/DynamicProgramming/BackpackModel/Dependent.py)
                - [背包问题求方案数](算法/Improve/DynamicProgramming/BackpackModel/PlanNumber.py)
                - [背包问题求具体方案](算法/Improve/DynamicProgramming/BackpackModel/SpecificPlan.py)
                - [能量石](算法/Improve/DynamicProgramming/BackpackModel/EnergyStone.py)
                - [金明的预算方案](算法/Improve/DynamicProgramming/BackpackModel/BudgetPlan.py)
          - [状态机模型](算法/Improve/DynamicProgramming/StateMachineModel)
              - [大盗阿福](算法/Improve/DynamicProgramming/StateMachineModel/ThiefAlfred.py)
              - [股票买卖 IV](算法/Improve/DynamicProgramming/StateMachineModel/StockTradingIV.py)
              - [股票买卖 V](算法/Improve/DynamicProgramming/StateMachineModel/StockTradingV.py)
              - [设计密码](算法/Improve/DynamicProgramming/StateMachineModel/DesignPassword.py)
              - [修复DNA](算法/Improve/DynamicProgramming/StateMachineModel/RepairDNA.py)
          - [状态压缩DP](算法/Improve/DynamicProgramming/StateCompressionDP)
              - [小国王](算法/Improve/DynamicProgramming/StateCompressionDP/LittleKing.py)
              - [玉米田](算法/Improve/DynamicProgramming/StateCompressionDP/Cornfield.py)
              - [炮兵阵地](算法/Improve/DynamicProgramming/StateCompressionDP/ArtilleryEmplacement.py)
              - [愤怒的小鸟](算法/Improve/DynamicProgramming/StateCompressionDP/AngryBirds.py)
              - [宝藏](算法/Improve/DynamicProgramming/StateCompressionDP/PreciousDeposits.py)
          - [区间DP](算法/Improve/DynamicProgramming/IntervalDP)
              - [环形石子合并](算法/Improve/DynamicProgramming/IntervalDP/RingPebblesMerge.py)
              - [能量项链](算法/Improve/DynamicProgramming/IntervalDP/EnergyNecklace.py)
              - [加分二叉树](算法/Improve/DynamicProgramming/IntervalDP/BonusBinaryTree.py)
              - [凸多边形的划分](算法/Improve/DynamicProgramming/IntervalDP/ConvexPolygonsDivision.py)
              - [棋盘分割](算法/Improve/DynamicProgramming/IntervalDP/CutUpChessboard.py)
          - [树形DP](算法/Improve/DynamicProgramming/TreeDP)
              - [树的最长路径](算法/Improve/DynamicProgramming/TreeDP/TreeLongestPath.py)
              - [树的中心](算法/Improve/DynamicProgramming/TreeDP/TreeCenter.py)
              - [数字转换](算法/Improve/DynamicProgramming/TreeDP/DigitalConversion.py)
              - [二叉苹果树](算法/Improve/DynamicProgramming/TreeDP/BinaryAppleTree.py)
              - [`战略游戏`](https://www.acwing.com/problem/content/325/)&#x2002;树形 DP + 状态机，由于读入不方便，放弃本题不写
              - [皇宫看守](算法/Improve/DynamicProgramming/TreeDP/PalaceGuard.py)
          - [数位DP](算法/Improve/DynamicProgramming/DigitalDP)
              - [度的数量](算法/Improve/DynamicProgramming/DigitalDP/NumberOfDegrees.py)
              - [数字游戏](算法/Improve/DynamicProgramming/DigitalDP/NumbersGame.py)
              - [Windy数](算法/Improve/DynamicProgramming/DigitalDP/WindyNumber.py)
    - [其他题解](算法/Other) &#x2002; 非系统性学习的题目