#*********************************************************************************************************************
#Author - Nirmallya Mukherjee
#This script will delete the code - commit, build, deploy, pipeline for the account
#*********************************************************************************************************************

# https://boto3.readthedocs.io/en/latest/reference/services/codebuild.html

import sys
import boto3

delete_mode = False
clientCC = boto3.client('codecommit')
clientCB = boto3.client('codebuild')
clientCD = boto3.client('codedeploy')
clientCP = boto3.client('codepipeline')

def cleanup_pipelines():
    print '\n*********************************************************************************************************************'
    print 'Looking for code pipelines',
    pipelineList = clientCP.list_pipelines()
    print pipelineList
    for item in pipelineList['pipelines']:
        piplineName = item['name']
        print 'Working on pipeline', piplineName,
        if delete_mode == True:
            clientCP.delete_pipeline(name=piplineName);
            print 'Deleted'
        else:
            print 'Skipped'
#End of function


def cleanup_codedeploys():
    print '\n*********************************************************************************************************************'
    print 'Looking for code deploys',
    appList = clientCD.list_applications()
    print appList
    for item in appList['applications']:
        print 'Working on application', item,
        if delete_mode == True:
            clientCD.delete_application(applicationName=item);
            print 'Deleted'
        else:
            print 'Skipped'
#End of function


def cleanup_codebuilds():
    print '\n*********************************************************************************************************************'
    print 'Looking for code builds',
    projList = clientCB.list_projects()
    print projList
    for item in projList['projects']:
        print 'Working on project', item,
        if delete_mode == True:
            clientCB.delete_project(name=item);
            print 'Deleted'
        else:
            print 'Skipped'
#End of function


def cleanup_codecommits():
    print '\n*********************************************************************************************************************'
    print 'Looking for code commits',
    repoList = clientCC.list_repositories()
    print repoList
    for item in repoList['repositories']:
        repoName = item['repositoryName'];
        print 'Working on repository', repoName,
        if delete_mode == True:
            clientCC.delete_repository(repositoryName=repoName);
            print 'Deleted'
        else:
            print 'Skipped'
#End of function


#Main app entry
def main():
    cleanup_pipelines()
    cleanup_codedeploys()
    cleanup_codebuilds()
    cleanup_codecommits()
#End of the function


delMod = sys.argv[1:]
print 'Delete mode passed is ', delMod[0],
if delMod[0] == 'true': delete_mode = True
print ' Global delete mode is now ', delete_mode
main()
