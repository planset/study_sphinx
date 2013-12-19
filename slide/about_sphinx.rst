
.. slide:: Sphinxとは

    * python製のドキュメントツール
 

.. slide:: ドキュメントツール？

    1. テキストで文章を書く
    2. Sphinxで変換する
    3. HTMLやPDFやEPUBができたー！！！


.. slide:: Sphinxの特徴1
 
    * 多くのフォーマットに変換
      html, epub, latex, pdf, man
 

.. slide:: Sphinxの特徴2
 
    * シンプルな記法(reStructuredText)
    * Wiki記法みたいな感じ::
      
        タイトル
        ========
        * 項目1
        * 項目2
 

.. slide:: Sphinxの特徴3

    * 機能を拡張することができる

      * テーマ
      * Sphinx拡張


.. slide:: では、

    Sphinxはどんなところに使えるの？


.. slide:: 開発系ドキュメント

    * もともとPythonの公式ドキュメントを作成するためのもの
    * 関数やクラスの説明を簡単に書ける
    * readthedocsによりgithubと連携してドキュメント生成もできる


.. slide:: ウェブサイト

    * HTML出力ができるので、動的な内容が必要でなければ割と十分使える。
    * sphinxの公式サイトもsphinxで出力されている。`link <http:://sphinx-doc.org>`_

.. slide:: その他色々

    * 議事録、技術メモ
    * そのままテキストで配布しても読める。


.. slide:: 書籍

    * エキスパートPythonプログラミング
    * Pythonプロフェッショナルプログラミング

    Sphinxからの出力を更に変換して
    ReVIEWフォーマットで出版だそうです。


.. slide:: Sphinxが不得意なこと

    * 図、表は別途作成する必要がある。
    * レイアウトをほとんど指定できない。
    * 変換しないと成果物を見ることができない。
    * (ビルドする環境が必要)
    * markdownじゃない


.. slide:: どのくらい使われているの？

    * `Sphinxを使用しているプロジェクト — Sphinx 1.1 (hg) documentation <http://sphinx-users.jp/doc11/examples.html>`_
    * `Sphinxを使用しているサイト — Python製ドキュメンテーションビルダー、Sphinxの日本ユーザ会 <http://sphinx-users.jp/example.html>`_


.. slide:: 実際に見てみましょう

    * 実際にサンプルを見てみましょう


