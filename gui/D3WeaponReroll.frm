VERSION 5.00
Begin VB.Form Form1 
   BorderStyle     =   1  'Fixed Single
   Caption         =   "武器附魔计算器"
   ClientHeight    =   6690
   ClientLeft      =   45
   ClientTop       =   375
   ClientWidth     =   5865
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   ScaleHeight     =   6690
   ScaleWidth      =   5865
   StartUpPosition =   3  '窗口缺省
   Begin VB.Frame Frame2 
      Caption         =   "武器白字估算值"
      Height          =   1215
      Left            =   120
      TabIndex        =   16
      Top             =   2520
      Width           =   5655
      Begin VB.Label Label_DMG_result 
         Alignment       =   2  'Center
         Caption         =   "0"
         BeginProperty Font 
            Name            =   "微软雅黑"
            Size            =   26.25
            Charset         =   134
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   855
         Left            =   120
         TabIndex        =   17
         Top             =   240
         Width           =   5295
      End
   End
   Begin VB.Frame Frame1 
      Caption         =   "可能洗出的结果"
      Height          =   2655
      Left            =   120
      TabIndex        =   15
      Top             =   3960
      Width           =   5655
      Begin VB.Label Label2 
         Alignment       =   1  'Right Justify
         Caption         =   "洗出7速时"
         Height          =   495
         Index           =   2
         Left            =   480
         TabIndex        =   23
         Top             =   1920
         Width           =   1215
      End
      Begin VB.Label Label2 
         Alignment       =   1  'Right Justify
         Caption         =   "洗出10ed时"
         Height          =   495
         Index           =   1
         Left            =   480
         TabIndex        =   22
         Top             =   1200
         Width           =   1215
      End
      Begin VB.Label Label2 
         Alignment       =   1  'Right Justify
         Caption         =   "白字洗到满时"
         Height          =   495
         Index           =   0
         Left            =   480
         TabIndex        =   21
         Top             =   480
         Width           =   1215
      End
      Begin VB.Label Label_Reroll_Result 
         Alignment       =   2  'Center
         Caption         =   "0"
         BeginProperty Font 
            Name            =   "微软雅黑"
            Size            =   26.25
            Charset         =   134
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   735
         Index           =   2
         Left            =   1560
         TabIndex        =   20
         Top             =   1680
         Width           =   4000
      End
      Begin VB.Label Label_Reroll_Result 
         Alignment       =   2  'Center
         Caption         =   "0"
         BeginProperty Font 
            Name            =   "微软雅黑"
            Size            =   26.25
            Charset         =   134
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   735
         Index           =   1
         Left            =   1560
         TabIndex        =   19
         Top             =   960
         Width           =   4000
      End
      Begin VB.Label Label_Reroll_Result 
         Alignment       =   2  'Center
         Caption         =   "0"
         BeginProperty Font 
            Name            =   "微软雅黑"
            Size            =   26.25
            Charset         =   134
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   735
         Index           =   0
         Left            =   1560
         TabIndex        =   18
         Top             =   240
         Width           =   4000
      End
   End
   Begin VB.ComboBox Combo2 
      Height          =   300
      ItemData        =   "D3WeaponReroll.frx":0000
      Left            =   4200
      List            =   "D3WeaponReroll.frx":0010
      Locked          =   -1  'True
      TabIndex        =   14
      Text            =   "0"
      Top             =   2040
      Width           =   1215
   End
   Begin VB.TextBox Text6 
      Height          =   270
      Left            =   2880
      TabIndex        =   11
      Text            =   "0"
      Top             =   2040
      Width           =   1215
   End
   Begin VB.TextBox Text4 
      Height          =   270
      Left            =   120
      TabIndex        =   9
      Text            =   "1385"
      Top             =   2040
      Width           =   1335
   End
   Begin VB.ComboBox Combo1 
      Height          =   300
      ItemData        =   "D3WeaponReroll.frx":0020
      Left            =   120
      List            =   "D3WeaponReroll.frx":0060
      Locked          =   -1  'True
      TabIndex        =   5
      Text            =   "单手钉锤"
      Top             =   840
      Width           =   1335
   End
   Begin VB.CheckBox Check1 
      Caption         =   "我这是远古的"
      Height          =   375
      Left            =   4200
      TabIndex        =   4
      Top             =   360
      Width           =   1455
   End
   Begin VB.TextBox Text5 
      Height          =   270
      Left            =   1560
      TabIndex        =   10
      Text            =   "1639"
      Top             =   2040
      Width           =   1215
   End
   Begin VB.Label Label5 
      BorderStyle     =   1  'Fixed Single
      Caption         =   "450.5"
      Height          =   255
      Left            =   4200
      TabIndex        =   27
      Top             =   840
      Width           =   1215
   End
   Begin VB.Label Label4 
      BorderStyle     =   1  'Fixed Single
      Caption         =   "450.5"
      Height          =   255
      Left            =   2880
      TabIndex        =   26
      Top             =   840
      Width           =   1215
   End
   Begin VB.Label LabelDMG 
      BorderStyle     =   1  'Fixed Single
      Caption         =   "450.5"
      Height          =   255
      Left            =   1560
      TabIndex        =   25
      Top             =   840
      Width           =   1215
   End
   Begin VB.Label Label3 
      Caption         =   "原作:/u/Krissam 转制:Oicebot"
      ForeColor       =   &H8000000A&
      Height          =   255
      Left            =   3000
      TabIndex        =   24
      Top             =   120
      Width           =   2655
   End
   Begin VB.Label TLabel 
      AutoSize        =   -1  'True
      Caption         =   "武器攻速词缀"
      Height          =   180
      Index           =   6
      Left            =   4200
      TabIndex        =   13
      Top             =   1680
      Width           =   1080
   End
   Begin VB.Label TLabel 
      AutoSize        =   -1  'True
      Caption         =   "增伤（ed）% "
      Height          =   180
      Index           =   5
      Left            =   2880
      TabIndex        =   12
      Top             =   1680
      Width           =   1080
   End
   Begin VB.Label TLabel 
      AutoSize        =   -1  'True
      Caption         =   "最高"
      Height          =   180
      Index           =   4
      Left            =   1560
      TabIndex        =   8
      Top             =   1680
      Width           =   360
   End
   Begin VB.Label TLabel 
      AutoSize        =   -1  'True
      Caption         =   "最低"
      Height          =   180
      Index           =   3
      Left            =   120
      TabIndex        =   7
      Top             =   1680
      Width           =   360
   End
   Begin VB.Label Label1 
      AutoSize        =   -1  'True
      Caption         =   "第二步，输入武器元素伤害："
      Height          =   180
      Index           =   1
      Left            =   120
      TabIndex        =   6
      Top             =   1320
      Width           =   2340
   End
   Begin VB.Label TLabel 
      AutoSize        =   -1  'True
      Caption         =   "武器基础攻速"
      Height          =   180
      Index           =   2
      Left            =   2880
      TabIndex        =   3
      Top             =   480
      Width           =   1080
   End
   Begin VB.Label Label1 
      AutoSize        =   -1  'True
      Caption         =   "第一步，选择武器类型："
      Height          =   180
      Index           =   0
      Left            =   120
      TabIndex        =   2
      Top             =   120
      Width           =   1980
   End
   Begin VB.Label TLabel 
      AutoSize        =   -1  'True
      Caption         =   "平均基础伤害"
      Height          =   180
      Index           =   1
      Left            =   1560
      TabIndex        =   1
      Top             =   480
      Width           =   1080
   End
   Begin VB.Label TLabel 
      AutoSize        =   -1  'True
      Caption         =   "武器类型"
      Height          =   180
      Index           =   0
      Left            =   120
      TabIndex        =   0
      Top             =   480
      Width           =   720
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub Form_Load()
  
End Sub
