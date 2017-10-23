using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Lab1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {
            OpenFileDialog OpenDlg = new OpenFileDialog();

            if (OpenDlg.ShowDialog() == DialogResult.OK)
            {
                StreamReader Reader = new StreamReader(OpenDlg.FileName, Encoding.Default);
                richTextBox1.Text = Reader.ReadToEnd();
                Reader.Close();
            }
            OpenDlg.Dispose();

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            listBox2.Items.Clear();
            richTextBox1.Text = "";
            checkBox1.Checked = true;
            checkBox2.Checked = false;
            radioButton1.Checked = true;
        }

        private void saveToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SaveFileDialog SaveDlg = new SaveFileDialog();

            if (SaveDlg.ShowDialog() == DialogResult.OK)
            {
                StreamWriter Writer = new StreamWriter(SaveDlg.FileName);
                for (int i = 0; i < listBox2.Items.Count; i++)
                {
                    Writer.WriteLine((string)listBox2.Items[i]);
                }
                Writer.Close();
            }
            SaveDlg.Dispose();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void helpToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Info");
        }

        private void button14_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button12_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            listBox2.Items.Clear();
            listBox1.BeginUpdate();
            string[] Strings = richTextBox1.Text.Split(new char[] { '\n', '\t', ' ' },
            StringSplitOptions.RemoveEmptyEntries);
            foreach (string s in Strings)
            {
                string Str = s.Trim();

                if (Str == String.Empty) continue;
                if (radioButton1.Checked) listBox1.Items.Add(Str);
                if (radioButton2.Checked)
                {
                    if (Regex.IsMatch(Str, @"\d")) listBox1.Items.Add(Str);
                }
                if (radioButton3.Checked)
                {
                    if (Regex.IsMatch(Str, @"\w+@\w+\.\w+")) listBox1.Items.Add(Str);
                }
            }
            listBox1.EndUpdate();
        }

        private void button11_Click(object sender, EventArgs e)
        {
            listBox3.Items.Clear();
            string Find = textBox1.Text;
            if (checkBox1.Checked)
            {
                foreach (string String in listBox1.Items)
                {
                    if (String.Contains(Find)) listBox3.Items.Add(String);
                }
            }
            if (checkBox2.Checked)
            {
                foreach (string String in listBox2.Items)
                {
                    if (String.Contains(Find)) listBox3.Items.Add(String);
                }
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Form2 AddRec = new Form2();
            AddRec.Owner = this;
            AddRec.ShowDialog();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            if (listBox1.IsHandleCreated)
            {
                this.DeleteSelectedStrings(listBox1);
            }

            if (listBox2.IsHandleCreated)
            {
                this.DeleteSelectedStrings(listBox2);
            }
        }

        private void DeleteSelectedStrings(ListBox ListBox)
        {
            for (int i = ListBox.Items.Count - 1; i >= 0; i--)
            {
                if (ListBox.GetSelected(i)) ListBox.Items.RemoveAt(i);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.ListBoxItemMigrate(listBox1, listBox2);
        }

        private void ListBoxItemMigrate(ListBox ListBoxFrom, ListBox ListBoxTo)
        {

            ListBoxTo.BeginUpdate();
            foreach (object Item in ListBoxFrom.SelectedItems)
            {
                ListBoxTo.Items.Add(Item);
            }
            ListBoxTo.EndUpdate();
            /*
            for (int i = ListBoxTo.Items.Count - 1; i >= 0; i--)
            {
                for (int j = ListBoxFrom.Items.Count - 1; i >= 0; i--)
                    if (ListBoxTo.Items.Equals(ListBoxFrom)) ListBoxFrom.Items.RemoveAt(j);
            }
            */
        }

        private void ListBoxItemsMigrate(ListBox ListBoxFrom, ListBox ListBoxTo)
        {
            ListBoxTo.Items.AddRange(ListBoxFrom.Items);
            ListBoxFrom.Items.Clear();        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.ListBoxItemsMigrate(listBox1, listBox2);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            this.ListBoxItemsMigrate(listBox2, listBox1);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.ListBoxItemMigrate(listBox2, listBox1);
        }

        private void ListBoxItemsClear(ListBox ListBox)
        {
            ListBox.Items.Clear();
        }

        private void button10_Click(object sender, EventArgs e)
        {
            this.ListBoxItemsClear(listBox1);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            this.ListBoxItemsClear(listBox2);
        }

        private void ListBoxSort(ListBox listBox, ComboBox comboBox)
        {
            /*
            if (comboBox.SelectedIndex == 0)
            {
                listBox.Sorted = true;
            }
            */
            listBox.Sorted = true;

        }

        private void button5_Click(object sender, EventArgs e)
        {
            this.ListBoxSort(listBox1, comboBox1);
        }
    }
}

/*
 * Сортировки
 * Перенос элементов списка
 */
